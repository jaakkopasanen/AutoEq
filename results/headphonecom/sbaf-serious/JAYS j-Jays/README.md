# JAYS j-Jays
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.3; 25 -11.3; 28 -11.4; 31 -11.4; 34 -11.5; 37 -11.5; 41 -11.6; 45 -11.7; 49 -11.7; 54 -11.9; 60 -12.2; 66 -12.5; 72 -12.6; 79 -12.9; 87 -13.0; 96 -13.2; 106 -13.3; 116 -13.3; 128 -13.4; 141 -13.6; 155 -13.5; 170 -13.3; 187 -13.1; 206 -12.7; 227 -12.2; 249 -11.8; 274 -12.0; 302 -11.4; 332 -10.7; 365 -9.9; 402 -9.2; 442 -8.8; 486 -8.1; 535 -7.5; 588 -6.9; 647 -6.4; 712 -6.1; 783 -6.0; 861 -6.0; 947 -6.3; 1042 -6.6; 1146 -7.0; 1261 -7.5; 1387 -8.2; 1526 -10.0; 1678 -10.7; 1846 -10.3; 2031 -9.3; 2234 -7.7; 2457 -5.5; 2703 -3.1; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -1.1; 4353 -5.8; 4788 -10.6; 5267 -6.2; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JAYS j-Jays GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JAYS j-Jays ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.23 | -4.6 dB |
| Peaking | 152 Hz   | 0.72 | -4.3 dB |
| Peaking | 293 Hz   | 1.96 | -2.0 dB |
| Peaking | 3380 Hz  | 3.39 | 7.2 dB  |
| Peaking | 21432 Hz | 2.3  | 3.7 dB  |
| Peaking | 799 Hz   | 1.88 | 1.5 dB  |
| Peaking | 1758 Hz  | 2.2  | -4.8 dB |
| Peaking | 2798 Hz  | 5.08 | 2.7 dB  |
| Peaking | 4854 Hz  | 7.58 | -7.3 dB |
| Peaking | 5989 Hz  | 3.81 | 6.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/JAYS%20j-Jays/JAYS%20j-Jays.png)