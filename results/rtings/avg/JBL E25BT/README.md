# JBL E25BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.4; 25 -5.6; 28 -6.0; 31 -6.2; 34 -6.4; 37 -6.6; 41 -6.8; 45 -6.9; 49 -7.0; 54 -7.3; 60 -7.7; 66 -8.1; 72 -8.4; 79 -8.8; 87 -9.2; 96 -9.6; 106 -10.1; 116 -10.5; 128 -10.8; 141 -11.1; 155 -11.2; 170 -11.1; 187 -11.0; 206 -10.9; 227 -10.5; 249 -10.0; 274 -9.4; 302 -8.7; 332 -8.2; 365 -7.7; 402 -7.1; 442 -6.3; 486 -5.6; 535 -4.7; 588 -3.8; 647 -2.8; 712 -1.8; 783 -0.9; 861 -0.5; 947 -1.2; 1042 -2.4; 1146 -3.3; 1261 -3.8; 1387 -4.0; 1526 -3.6; 1678 -3.3; 1846 -3.4; 2031 -3.5; 2234 -3.0; 2457 -2.6; 2703 -3.2; 2973 -4.7; 3270 -6.1; 3597 -6.7; 3957 -6.7; 4353 -7.0; 4788 -7.0; 5267 -7.8; 5793 -9.9; 6373 -12.3; 7010 -10.0; 7711 -6.1; 8482 -5.7; 9330 -9.0; 10263 -9.2; 11289 -4.3; 12418 -1.9; 13660 -3.0; 15026 -9.2; 16529 -13.3; 18182 -12.9; 20000 -12.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E25BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E25BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 68 Hz    | 0.31 | -4.9 dB  |
| Peaking | 200 Hz   | 0.7  | -6.4 dB  |
| Peaking | 6149 Hz  | 0.96 | -8.0 dB  |
| Peaking | 16741 Hz | 2.04 | -9.0 dB  |
| Peaking | 19492 Hz | 0.93 | -10.2 dB |
| Peaking | 818 Hz   | 1.89 | 6.1 dB   |
| Peaking | 854 Hz   | 0.87 | -3.2 dB  |
| Peaking | 8144 Hz  | 5.69 | 4.5 dB   |
| Peaking | 9914 Hz  | 2.64 | -5.2 dB  |
| Peaking | 12219 Hz | 2.96 | 5.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -7.5 dB  |
| Peaking | 250 Hz   | 1.41 | -7.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.8 dB  |
| Peaking | 16000 Hz | 1.41 | -10.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E25BT/JBL%20E25BT.png)