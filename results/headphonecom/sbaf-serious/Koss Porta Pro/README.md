# Koss Porta Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.5; 34 -2.5; 37 -3.3; 41 -4.4; 45 -5.3; 49 -6.2; 54 -7.2; 60 -8.2; 66 -9.2; 72 -10.0; 79 -10.8; 87 -11.4; 96 -12.0; 106 -12.4; 116 -12.4; 128 -12.5; 141 -12.4; 155 -12.4; 170 -12.2; 187 -11.8; 206 -11.3; 227 -10.9; 249 -10.4; 274 -10.0; 302 -9.6; 332 -9.1; 365 -8.6; 402 -8.1; 442 -7.8; 486 -7.4; 535 -7.1; 588 -6.8; 647 -6.5; 712 -6.5; 783 -6.3; 861 -6.4; 947 -6.5; 1042 -6.6; 1146 -6.8; 1261 -7.2; 1387 -7.9; 1526 -8.9; 1678 -9.8; 1846 -10.6; 2031 -11.2; 2234 -11.0; 2457 -9.5; 2703 -7.2; 2973 -4.7; 3270 -3.1; 3597 -2.4; 3957 -4.9; 4353 -6.2; 4788 -7.7; 5267 -5.5; 5793 -2.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -9.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.63 | 7.5 dB  |
| Peaking | 117 Hz  | 0.45 | -7.0 dB |
| Peaking | 2071 Hz | 1.09 | -8.7 dB |
| Peaking | 2148 Hz | 0.35 | 3.8 dB  |
| Peaking | 3267 Hz | 3.59 | 4.7 dB  |
| Peaking | 4791 Hz | 5.55 | -3.2 dB |
| Peaking | 6216 Hz | 4.85 | 5.2 dB  |
| Peaking | 9083 Hz | 4.64 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)