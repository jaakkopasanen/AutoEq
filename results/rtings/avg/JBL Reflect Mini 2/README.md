# JBL Reflect Mini 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -8.5; 25 -8.3; 28 -8.1; 31 -7.8; 34 -7.7; 37 -7.6; 41 -7.5; 45 -7.4; 49 -7.4; 54 -7.4; 60 -7.4; 66 -7.5; 72 -7.6; 79 -7.6; 87 -7.7; 96 -7.7; 106 -7.6; 116 -7.6; 128 -7.5; 141 -7.2; 155 -7.0; 170 -6.7; 187 -6.3; 206 -6.1; 227 -5.8; 249 -5.5; 274 -5.0; 302 -4.6; 332 -4.1; 365 -3.7; 402 -3.3; 442 -2.8; 486 -2.4; 535 -1.8; 588 -1.3; 647 -0.8; 712 -0.6; 783 -0.5; 861 -0.6; 947 -1.2; 1042 -2.0; 1146 -3.0; 1261 -3.7; 1387 -4.1; 1526 -4.2; 1678 -4.4; 1846 -4.6; 2031 -5.2; 2234 -6.5; 2457 -7.5; 2703 -6.8; 2973 -4.5; 3270 -2.8; 3597 -2.2; 3957 -2.1; 4353 -2.3; 4788 -2.5; 5267 -1.9; 5793 -1.7; 6373 -3.6; 7010 -9.6; 7711 -10.1; 8482 -4.7; 9330 -4.1; 10263 -4.1; 11289 -8.0; 12418 -9.8; 13660 -5.7; 15026 -4.1; 16529 -6.5; 18182 -9.9; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Reflect Mini 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Reflect Mini 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.11 | -3.9 dB  |
| Peaking | 681 Hz   | 1.32 | 4.3 dB   |
| Peaking | 12191 Hz | 3.88 | -6.2 dB  |
| Peaking | 17679 Hz | 3.28 | -4.2 dB  |
| Peaking | 18566 Hz | 2.4  | -4.7 dB  |
| Peaking | 16 Hz    | 2.86 | -0.8 dB  |
| Peaking | 2454 Hz  | 2.72 | -4.8 dB  |
| Peaking | 6766 Hz  | 0.61 | 4.6 dB   |
| Peaking | 7397 Hz  | 3.87 | -11.5 dB |
| Peaking | 11688 Hz | 2.46 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Reflect%20Mini%202/JBL%20Reflect%20Mini%202.png)