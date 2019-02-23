# JAYS j-Jays
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.4; 23 -10.5; 25 -10.6; 28 -10.6; 31 -10.7; 34 -10.7; 37 -10.8; 41 -10.9; 45 -11.0; 49 -11.0; 54 -11.2; 60 -11.5; 66 -11.7; 72 -11.8; 79 -12.1; 87 -12.3; 96 -12.5; 106 -12.5; 116 -12.6; 128 -12.6; 141 -12.8; 155 -12.8; 170 -12.6; 187 -12.4; 206 -11.9; 227 -11.5; 249 -11.1; 274 -11.3; 302 -10.7; 332 -10.0; 365 -9.2; 402 -8.5; 442 -8.0; 486 -7.4; 535 -6.8; 588 -6.2; 647 -5.7; 712 -5.3; 783 -5.2; 861 -5.2; 947 -5.6; 1042 -5.9; 1146 -6.3; 1261 -6.8; 1387 -7.5; 1526 -9.2; 1678 -9.9; 1846 -9.5; 2031 -8.5; 2234 -7.0; 2457 -4.8; 2703 -2.4; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -5.1; 4788 -9.8; 5267 -5.4; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JAYS j-Jays GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JAYS j-Jays ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.33 | -4.2 dB |
| Peaking | 149 Hz   | 0.92 | -4.2 dB |
| Peaking | 284 Hz   | 2.4  | -2.3 dB |
| Peaking | 3376 Hz  | 2.77 | 7.1 dB  |
| Peaking | 21400 Hz | 2.45 | 3.4 dB  |
| Peaking | 815 Hz   | 1.72 | 2.0 dB  |
| Peaking | 1759 Hz  | 2.39 | -4.3 dB |
| Peaking | 2767 Hz  | 5.93 | 2.5 dB  |
| Peaking | 4865 Hz  | 7.78 | -6.9 dB |
| Peaking | 5977 Hz  | 3.77 | 6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/JAYS%20j-Jays/JAYS%20j-Jays.png)