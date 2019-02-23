# Beyerdynamic DT 1350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.2; 25 -8.3; 28 -8.3; 31 -8.4; 34 -8.5; 37 -8.5; 41 -8.6; 45 -8.6; 49 -8.7; 54 -8.5; 60 -8.5; 66 -8.9; 72 -9.1; 79 -9.2; 87 -8.8; 96 -8.0; 106 -7.4; 116 -8.0; 128 -8.1; 141 -7.1; 155 -7.5; 170 -8.5; 187 -9.8; 206 -10.4; 227 -10.6; 249 -10.7; 274 -10.5; 302 -10.2; 332 -10.9; 365 -11.1; 402 -10.7; 442 -10.9; 486 -11.0; 535 -10.6; 588 -10.0; 647 -9.5; 712 -8.5; 783 -7.7; 861 -7.7; 947 -7.3; 1042 -6.7; 1146 -6.1; 1261 -5.7; 1387 -5.8; 1526 -6.2; 1678 -6.7; 1846 -6.6; 2031 -5.5; 2234 -3.4; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.7; 4353 -4.8; 4788 -4.4; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.8; 8482 -13.9; 9330 -15.8; 10263 -8.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 43 Hz   | 0.61 | -2.2 dB  |
| Peaking | 364 Hz  | 0.74 | -4.7 dB  |
| Peaking | 3003 Hz | 1.77 | 6.7 dB   |
| Peaking | 6083 Hz | 2.73 | 6.4 dB   |
| Peaking | 8993 Hz | 4.39 | -11.7 dB |
| Peaking | 152 Hz  | 4.27 | 1.5 dB   |
| Peaking | 200 Hz  | 3.85 | -1.3 dB  |
| Peaking | 1282 Hz | 2.27 | 1.8 dB   |
| Peaking | 1829 Hz | 1.67 | -2.0 dB  |
| Peaking | 2445 Hz | 6.04 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -4.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%201350/Beyerdynamic%20DT%201350.png)