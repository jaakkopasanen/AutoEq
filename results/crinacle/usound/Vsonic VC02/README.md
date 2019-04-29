# Vsonic VC02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.6; 25 -5.9; 28 -6.4; 31 -6.7; 34 -7.0; 37 -7.2; 41 -7.5; 45 -7.7; 49 -7.9; 54 -8.1; 60 -8.4; 66 -8.8; 72 -9.1; 79 -9.5; 87 -9.9; 96 -10.3; 106 -10.6; 116 -10.9; 128 -11.2; 141 -11.4; 155 -11.6; 170 -11.6; 187 -11.6; 206 -11.6; 227 -11.5; 249 -11.3; 274 -11.2; 302 -10.9; 332 -10.7; 365 -10.4; 402 -10.1; 442 -9.8; 486 -9.4; 535 -9.0; 588 -8.6; 647 -8.1; 712 -7.6; 783 -7.0; 861 -6.6; 947 -6.5; 1042 -6.4; 1146 -7.1; 1261 -8.1; 1387 -8.6; 1526 -8.0; 1678 -6.6; 1846 -4.3; 2031 -4.7; 2234 -3.8; 2457 -2.4; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.7; 8482 -11.5; 9330 -10.6; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vsonic VC02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vsonic VC02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 124 Hz   | 0.7  | -3.3 dB |
| Peaking | 292 Hz   | 0.64 | -3.6 dB |
| Peaking | 1443 Hz  | 3.07 | -3.9 dB |
| Peaking | 4375 Hz  | 0.57 | 7.1 dB  |
| Peaking | 8748 Hz  | 3.09 | -9.2 dB |
| Peaking | 20 Hz    | 2.16 | 1.4 dB  |
| Peaking | 2847 Hz  | 4.88 | 1.7 dB  |
| Peaking | 3763 Hz  | 0.89 | -0.7 dB |
| Peaking | 6206 Hz  | 5.03 | 1.7 dB  |
| Peaking | 14906 Hz | 2.35 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Vsonic%20VC02/Vsonic%20VC02.png)