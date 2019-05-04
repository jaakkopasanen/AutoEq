# Audeze Sine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.2; 25 -1.3; 28 -1.4; 31 -1.5; 34 -1.5; 37 -1.6; 41 -1.7; 45 -1.9; 49 -2.1; 54 -2.4; 60 -2.9; 66 -3.3; 72 -3.6; 79 -3.8; 87 -4.2; 96 -4.8; 106 -5.2; 116 -5.6; 128 -5.9; 141 -6.1; 155 -6.4; 170 -6.4; 187 -6.2; 206 -6.0; 227 -6.4; 249 -6.7; 274 -6.9; 302 -7.0; 332 -6.9; 365 -6.8; 402 -6.7; 442 -7.0; 486 -7.1; 535 -7.0; 588 -6.9; 647 -6.7; 712 -6.6; 783 -6.6; 861 -6.7; 947 -6.9; 1042 -7.2; 1146 -7.5; 1261 -7.7; 1387 -7.7; 1526 -7.3; 1678 -7.2; 1846 -7.5; 2031 -7.6; 2234 -7.2; 2457 -6.4; 2703 -6.6; 2973 -6.8; 3270 -7.1; 3597 -7.0; 3957 -5.4; 4353 -3.2; 4788 -2.4; 5267 -2.2; 5793 -1.5; 6373 -0.5; 7010 -3.2; 7711 -5.4; 8482 -5.7; 9330 -5.8; 10263 -10.7; 11289 -12.9; 12418 -13.5; 13660 -18.6; 15026 -26.1; 16529 -31.0; 18182 -30.5; 20000 -25.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.97 | 4.4 dB   |
| Peaking | 51 Hz    | 1.44 | 2.5 dB   |
| Peaking | 2556 Hz  | 0.33 | -8.1 dB  |
| Peaking | 6615 Hz  | 0.34 | 21.9 dB  |
| Peaking | 17023 Hz | 0.29 | -33.2 dB |
| Peaking | 260 Hz   | 1.05 | -0.8 dB  |
| Peaking | 3526 Hz  | 2.83 | -3.3 dB  |
| Peaking | 4099 Hz  | 0.76 | 1.7 dB   |
| Peaking | 7585 Hz  | 6.81 | -2.8 dB  |
| Peaking | 12691 Hz | 7.49 | 2.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB   |
| Peaking | 62 Hz    | 1.41 | 2.2 dB   |
| Peaking | 125 Hz   | 1.41 | -0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 9.4 dB   |
| Peaking | 16000 Hz | 1.41 | -35.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Audeze%20Sine/Audeze%20Sine.png)