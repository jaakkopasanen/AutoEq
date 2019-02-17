# Yuin G2A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.1; 49 -1.9; 54 -2.8; 60 -3.7; 66 -4.5; 72 -5.0; 79 -5.3; 87 -6.1; 96 -6.7; 106 -7.2; 116 -7.6; 128 -8.0; 141 -8.5; 155 -8.7; 170 -8.6; 187 -8.6; 206 -8.4; 227 -8.4; 249 -8.2; 274 -8.3; 302 -8.0; 332 -7.8; 365 -7.6; 402 -7.2; 442 -7.2; 486 -6.8; 535 -6.7; 588 -6.4; 647 -6.2; 712 -6.3; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -7.1; 1387 -7.8; 1526 -8.4; 1678 -9.5; 1846 -10.4; 2031 -11.1; 2234 -10.9; 2457 -9.7; 2703 -7.3; 2973 -4.3; 3270 -1.8; 3597 -0.6; 3957 -4.7; 4353 -10.9; 4788 -13.2; 5267 -10.5; 5793 -4.0; 6373 -1.0; 7010 -4.0; 7711 -7.8; 8482 -11.6; 9330 -12.7; 10263 -9.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin G2A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin G2A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.16 | 7.1 dB   |
| Peaking | 2260 Hz  | 1.09 | -13.7 dB |
| Peaking | 3677 Hz  | 0.69 | 16.1 dB  |
| Peaking | 4648 Hz  | 3.5  | -17.9 dB |
| Peaking | 9084 Hz  | 2.94 | -10.3 dB |
| Peaking | 52 Hz    | 1.81 | 1.8 dB   |
| Peaking | 174 Hz   | 0.81 | -2.5 dB  |
| Peaking | 5350 Hz  | 9.32 | -3.7 dB  |
| Peaking | 6262 Hz  | 6.24 | 4.4 dB   |
| Peaking | 20138 Hz | 0.08 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20G2A/Yuin%20G2A.png)