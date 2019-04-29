# Jomo Jazz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.8; 25 -5.0; 28 -5.3; 31 -5.6; 34 -5.8; 37 -6.0; 41 -6.2; 45 -6.4; 49 -6.5; 54 -6.8; 60 -7.1; 66 -7.4; 72 -7.7; 79 -8.0; 87 -8.4; 96 -8.8; 106 -9.2; 116 -9.5; 128 -9.7; 141 -10.0; 155 -10.1; 170 -10.2; 187 -10.2; 206 -10.1; 227 -10.0; 249 -10.0; 274 -9.8; 302 -9.4; 332 -9.1; 365 -8.8; 402 -8.4; 442 -8.0; 486 -7.6; 535 -7.2; 588 -6.7; 647 -6.3; 712 -5.8; 783 -5.4; 861 -5.1; 947 -5.2; 1042 -5.8; 1146 -7.0; 1261 -8.6; 1387 -10.0; 1526 -10.6; 1678 -9.1; 1846 -6.6; 2031 -4.5; 2234 -3.3; 2457 -2.6; 2703 -2.2; 2973 -1.7; 3270 -1.1; 3597 -1.3; 3957 -1.6; 4353 -2.2; 4788 -4.3; 5267 -8.3; 5793 -4.7; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Jazz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Jazz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 11 Hz   | 0.32 | 1.8 dB   |
| Peaking | 203 Hz  | 0.41 | -4.6 dB  |
| Peaking | 1502 Hz | 1.84 | -11.0 dB |
| Peaking | 1684 Hz | 0.54 | 6.5 dB   |
| Peaking | 3504 Hz | 2.78 | 2.5 dB   |
| Peaking | 4450 Hz | 4.82 | 1.6 dB   |
| Peaking | 5425 Hz | 5    | -6.5 dB  |
| Peaking | 6350 Hz | 4.05 | 6.9 dB   |
| Peaking | 7533 Hz | 1.7  | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Jazz/Jomo%20Jazz.png)