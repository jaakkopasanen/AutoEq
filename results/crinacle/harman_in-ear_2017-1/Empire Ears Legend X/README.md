# Empire Ears Legend X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.5; 23 -14.5; 25 -14.5; 28 -14.4; 31 -14.3; 34 -14.2; 37 -14.2; 41 -14.1; 45 -14.0; 49 -13.9; 54 -13.7; 60 -13.6; 66 -13.5; 72 -13.4; 79 -13.4; 87 -13.3; 96 -13.3; 106 -13.2; 116 -13.0; 128 -12.9; 141 -12.6; 155 -12.4; 170 -12.0; 187 -11.7; 206 -11.3; 227 -10.8; 249 -10.3; 274 -9.9; 302 -9.3; 332 -8.7; 365 -8.1; 402 -7.6; 442 -7.1; 486 -6.7; 535 -6.2; 588 -5.8; 647 -5.3; 712 -4.8; 783 -4.1; 861 -3.9; 947 -4.3; 1042 -5.2; 1146 -6.2; 1261 -7.1; 1387 -7.6; 1526 -7.9; 1678 -7.9; 1846 -7.7; 2031 -7.0; 2234 -5.9; 2457 -4.4; 2703 -3.0; 2973 -1.9; 3270 -1.0; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -0.5; 5267 -0.6; 5793 -2.2; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -17.1; 15026 -27.4; 16529 -30.4; 18182 -28.0; 20000 -20.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Legend X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Legend X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.23 | -7.7 dB  |
| Peaking | 153 Hz   | 0.64 | -3.8 dB  |
| Peaking | 772 Hz   | 3.18 | 2.7 dB   |
| Peaking | 8744 Hz  | 0.37 | 13.2 dB  |
| Peaking | 16749 Hz | 0.55 | -31.7 dB |
| Peaking | 1800 Hz  | 1.08 | -8.3 dB  |
| Peaking | 2423 Hz  | 0.46 | 5.3 dB   |
| Peaking | 8311 Hz  | 2.15 | -5.1 dB  |
| Peaking | 12484 Hz | 2.59 | 7.6 dB   |
| Peaking | 14610 Hz | 3.04 | -7.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.2 dB  |
| Peaking | 62 Hz    | 1.41 | -5.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 16000 Hz | 1.41 | -28.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Empire%20Ears%20Legend%20X/Empire%20Ears%20Legend%20X.png)