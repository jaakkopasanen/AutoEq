# Philips SHE 8000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.6; 23 -9.4; 25 -10.1; 28 -10.9; 31 -11.5; 34 -12.0; 37 -12.4; 41 -12.7; 45 -13.0; 49 -13.3; 54 -13.4; 60 -13.6; 66 -13.7; 72 -13.8; 79 -13.8; 87 -13.7; 96 -13.5; 106 -13.4; 116 -13.3; 128 -13.1; 141 -12.8; 155 -12.5; 170 -12.2; 187 -11.9; 206 -11.5; 227 -11.1; 249 -10.5; 274 -10.0; 302 -9.5; 332 -8.9; 365 -8.3; 402 -7.5; 442 -6.8; 486 -6.5; 535 -6.1; 588 -5.5; 647 -4.7; 712 -4.0; 783 -3.2; 861 -2.4; 947 -1.6; 1042 -0.8; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.8; 2703 -3.3; 2973 -6.6; 3270 -8.8; 3597 -8.9; 3957 -8.0; 4353 -7.3; 4788 -7.6; 5267 -9.3; 5793 -11.7; 6373 -12.0; 7010 -9.4; 7711 -6.3; 8482 -6.5; 9330 -7.1; 10263 -7.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHE 8000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHE 8000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 86 Hz    | 0.28 | -7.3 dB |
| Peaking | 1756 Hz  | 0.45 | 7.4 dB  |
| Peaking | 3406 Hz  | 2.59 | -7.4 dB |
| Peaking | 6032 Hz  | 2.69 | -7.6 dB |
| Peaking | 17 Hz    | 2.22 | 1.4 dB  |
| Peaking | 1673 Hz  | 4.18 | -0.7 dB |
| Peaking | 2422 Hz  | 8.35 | 1.4 dB  |
| Peaking | 7797 Hz  | 7.94 | 1.4 dB  |
| Peaking | 10011 Hz | 7.48 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.2 dB |
| Peaking | 62 Hz    | 1.41 | -6.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.9 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20SHE%208000/Philips%20SHE%208000.png)