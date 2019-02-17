# Massdrop Plus Universal IEM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.4; 25 -5.5; 28 -5.6; 31 -5.6; 34 -5.7; 37 -5.8; 41 -5.9; 45 -6.1; 49 -6.2; 54 -6.3; 60 -6.5; 66 -6.8; 72 -7.0; 79 -7.3; 87 -7.5; 96 -7.8; 106 -8.0; 116 -8.2; 128 -8.3; 141 -8.4; 155 -8.4; 170 -8.3; 187 -8.1; 206 -7.9; 227 -7.6; 249 -7.3; 274 -7.0; 302 -6.6; 332 -6.0; 365 -5.5; 402 -5.1; 442 -4.9; 486 -4.7; 535 -4.3; 588 -3.9; 647 -3.6; 712 -3.3; 783 -3.0; 861 -3.0; 947 -3.3; 1042 -3.9; 1146 -4.5; 1261 -5.1; 1387 -5.5; 1526 -5.9; 1678 -6.1; 1846 -6.2; 2031 -6.1; 2234 -5.6; 2457 -4.7; 2703 -3.8; 2973 -3.0; 3270 -2.6; 3597 -2.6; 3957 -2.9; 4353 -3.3; 4788 -2.9; 5267 -1.7; 5793 -0.7; 6373 -0.5; 7010 -2.6; 7711 -4.7; 8482 -4.7; 9330 -3.7; 10263 -3.7; 11289 -3.7; 12418 -3.7; 13660 -10.3; 15026 -20.8; 16529 -18.3; 18182 -8.3; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop Plus Universal IEM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Plus Universal IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 60 Hz    | 0.37 | -2.2 dB  |
| Peaking | 170 Hz   | 0.76 | -3.6 dB  |
| Peaking | 1832 Hz  | 2.04 | -3.2 dB  |
| Peaking | 10696 Hz | 0.38 | 3.4 dB   |
| Peaking | 15651 Hz | 1.76 | -22.1 dB |
| Peaking | 785 Hz   | 3.19 | 1.3 dB   |
| Peaking | 6315 Hz  | 4.19 | 2.8 dB   |
| Peaking | 7939 Hz  | 2.8  | -3.2 dB  |
| Peaking | 12872 Hz | 3.24 | 4.9 dB   |
| Peaking | 14416 Hz | 4.91 | -5.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 16000 Hz | 1.41 | -16.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Massdrop%20Plus%20Universal%20IEM/Massdrop%20Plus%20Universal%20IEM.png)