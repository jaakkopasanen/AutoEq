# JAYS q-Jays
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.5; 25 -6.5; 28 -6.6; 31 -6.8; 34 -6.9; 37 -6.9; 41 -7.0; 45 -7.2; 49 -7.3; 54 -7.5; 60 -7.8; 66 -8.0; 72 -8.2; 79 -8.5; 87 -8.8; 96 -9.1; 106 -9.4; 116 -9.6; 128 -9.6; 141 -10.0; 155 -10.2; 170 -10.4; 187 -10.5; 206 -10.4; 227 -10.4; 249 -10.2; 274 -10.2; 302 -9.9; 332 -9.5; 365 -9.6; 402 -9.7; 442 -9.4; 486 -9.0; 535 -8.7; 588 -8.2; 647 -8.0; 712 -7.8; 783 -7.6; 861 -7.5; 947 -7.6; 1042 -7.8; 1146 -7.9; 1261 -7.9; 1387 -8.2; 1526 -9.0; 1678 -9.9; 1846 -9.8; 2031 -9.4; 2234 -8.6; 2457 -7.2; 2703 -4.7; 2973 -1.2; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.6; 9330 -13.5; 10263 -8.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JAYS q-Jays GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JAYS q-Jays ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 162 Hz   | 0.56 | -3.1 dB  |
| Peaking | 390 Hz   | 0.59 | -1.7 dB  |
| Peaking | 1996 Hz  | 1.15 | -9.4 dB  |
| Peaking | 3636 Hz  | 0.54 | 9.5 dB   |
| Peaking | 9170 Hz  | 3.27 | -10.6 dB |
| Peaking | 2591 Hz  | 6.05 | -1.4 dB  |
| Peaking | 3051 Hz  | 4.66 | 2.0 dB   |
| Peaking | 4137 Hz  | 2.42 | -1.0 dB  |
| Peaking | 6145 Hz  | 7    | 1.5 dB   |
| Peaking | 14627 Hz | 2.03 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 9.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/JAYS%20q-Jays/JAYS%20q-Jays.png)