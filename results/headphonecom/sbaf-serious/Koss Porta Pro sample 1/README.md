# Koss Porta Pro sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.5; 34 -2.5; 37 -3.4; 41 -4.4; 45 -5.4; 49 -6.2; 54 -7.3; 60 -8.3; 66 -9.2; 72 -10.0; 79 -10.8; 87 -11.4; 96 -12.0; 106 -12.4; 116 -12.4; 128 -12.5; 141 -12.4; 155 -12.5; 170 -12.2; 187 -12.0; 206 -11.5; 227 -11.0; 249 -10.4; 274 -10.0; 302 -9.5; 332 -9.0; 365 -8.6; 402 -8.2; 442 -7.9; 486 -7.3; 535 -7.1; 588 -6.8; 647 -6.4; 712 -6.5; 783 -6.3; 861 -6.4; 947 -6.5; 1042 -6.6; 1146 -6.8; 1261 -7.2; 1387 -7.9; 1526 -9.0; 1678 -9.8; 1846 -10.7; 2031 -11.1; 2234 -10.8; 2457 -9.0; 2703 -6.7; 2973 -3.9; 3270 -2.3; 3597 -1.6; 3957 -4.9; 4353 -5.8; 4788 -6.6; 5267 -4.0; 5793 -1.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.7; 9330 -8.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.8; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.7  | 7.4 dB  |
| Peaking | 121 Hz   | 0.48 | -6.9 dB |
| Peaking | 2038 Hz  | 1.1  | -9.9 dB |
| Peaking | 2312 Hz  | 0.4  | 5.1 dB  |
| Peaking | 3264 Hz  | 3.87 | 4.6 dB  |
| Peaking | 4744 Hz  | 4.25 | -3.2 dB |
| Peaking | 6050 Hz  | 3.57 | 5.2 dB  |
| Peaking | 8875 Hz  | 3.52 | -3.7 dB |
| Peaking | 20205 Hz | 2.77 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20Porta%20Pro%20sample%201/Koss%20Porta%20Pro%20sample%201.png)