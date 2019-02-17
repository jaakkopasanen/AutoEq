# Koss Porta Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.6; 31 -2.7; 34 -3.7; 37 -4.5; 41 -5.5; 45 -6.3; 49 -7.1; 54 -7.8; 60 -8.6; 66 -9.3; 72 -9.9; 79 -10.5; 87 -11.0; 96 -11.5; 106 -11.8; 116 -12.1; 128 -12.3; 141 -12.4; 155 -12.4; 170 -12.2; 187 -11.9; 206 -11.5; 227 -11.0; 249 -10.7; 274 -10.4; 302 -10.2; 332 -9.9; 365 -9.6; 402 -9.3; 442 -9.1; 486 -8.8; 535 -8.5; 588 -8.1; 647 -7.7; 712 -7.3; 783 -6.9; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.8; 1261 -7.3; 1387 -7.9; 1526 -8.6; 1678 -9.2; 1846 -10.0; 2031 -10.5; 2234 -10.1; 2457 -8.9; 2703 -7.6; 2973 -7.4; 3270 -7.9; 3597 -7.2; 3957 -2.4; 4353 -0.5; 4788 -5.1; 5267 -10.3; 5793 -6.0; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.87 | 6.9 dB  |
| Peaking | 134 Hz  | 0.46 | -6.1 dB |
| Peaking | 2164 Hz | 1.94 | -4.9 dB |
| Peaking | 2478 Hz | 3.48 | 1.7 dB  |
| Peaking | 4254 Hz | 7.19 | 7.5 dB  |
| Peaking | 947 Hz  | 3.32 | 1.1 dB  |
| Peaking | 4633 Hz | 8.77 | 3.3 dB  |
| Peaking | 5269 Hz | 5.59 | -5.3 dB |
| Peaking | 6060 Hz | 1.16 | -1.2 dB |
| Peaking | 6431 Hz | 4.07 | 6.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)