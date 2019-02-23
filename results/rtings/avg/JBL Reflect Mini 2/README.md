# JBL Reflect Mini 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -3.8; 25 -3.6; 28 -3.3; 31 -3.1; 34 -2.9; 37 -2.8; 41 -2.7; 45 -2.6; 49 -2.6; 54 -2.7; 60 -3.1; 66 -3.4; 72 -3.7; 79 -3.9; 87 -4.3; 96 -4.6; 106 -5.1; 116 -5.5; 128 -5.8; 141 -6.1; 155 -6.2; 170 -6.2; 187 -6.1; 206 -6.1; 227 -6.0; 249 -5.6; 274 -5.2; 302 -4.7; 332 -4.3; 365 -3.9; 402 -3.4; 442 -2.9; 486 -2.4; 535 -1.8; 588 -1.3; 647 -0.8; 712 -0.6; 783 -0.5; 861 -0.6; 947 -1.2; 1042 -2.0; 1146 -2.9; 1261 -3.6; 1387 -4.0; 1526 -4.1; 1678 -4.3; 1846 -4.4; 2031 -4.9; 2234 -5.7; 2457 -6.7; 2703 -6.3; 2973 -4.5; 3270 -3.1; 3597 -2.6; 3957 -2.5; 4353 -2.8; 4788 -2.2; 5267 -1.6; 5793 -1.9; 6373 -4.7; 7010 -9.5; 7711 -9.5; 8482 -4.7; 9330 -4.0; 10263 -4.0; 11289 -6.9; 12418 -9.6; 13660 -6.5; 15026 -4.0; 16529 -6.7; 18182 -10.1; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Reflect Mini 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Reflect Mini 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 754 Hz   | 1.86 | 4.0 dB   |
| Peaking | 2467 Hz  | 5    | -3.2 dB  |
| Peaking | 12433 Hz | 3.64 | -5.8 dB  |
| Peaking | 17650 Hz | 3.08 | -4.5 dB  |
| Peaking | 18697 Hz | 2.27 | -4.8 dB  |
| Peaking | 47 Hz    | 1.17 | 1.7 dB   |
| Peaking | 168 Hz   | 1.1  | -2.6 dB  |
| Peaking | 5866 Hz  | 1.62 | 4.8 dB   |
| Peaking | 7288 Hz  | 2.95 | -10.4 dB |
| Peaking | 8790 Hz  | 2.42 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -3.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Reflect%20Mini%202/JBL%20Reflect%20Mini%202.png)