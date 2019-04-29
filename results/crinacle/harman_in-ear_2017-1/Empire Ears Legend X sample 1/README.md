# Empire Ears Legend X sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.1; 23 -14.1; 25 -14.1; 28 -14.1; 31 -14.0; 34 -13.9; 37 -13.9; 41 -13.8; 45 -13.7; 49 -13.6; 54 -13.5; 60 -13.3; 66 -13.3; 72 -13.3; 79 -13.3; 87 -13.3; 96 -13.3; 106 -13.2; 116 -13.1; 128 -12.9; 141 -12.7; 155 -12.5; 170 -12.2; 187 -11.8; 206 -11.4; 227 -11.0; 249 -10.5; 274 -10.0; 302 -9.5; 332 -8.8; 365 -8.2; 402 -7.7; 442 -7.2; 486 -6.7; 535 -6.2; 588 -5.8; 647 -5.4; 712 -4.7; 783 -3.8; 861 -3.6; 947 -4.0; 1042 -4.9; 1146 -6.0; 1261 -6.9; 1387 -7.4; 1526 -7.7; 1678 -7.7; 1846 -7.6; 2031 -6.9; 2234 -5.7; 2457 -4.3; 2703 -2.9; 2973 -1.8; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -1.8; 4788 -0.5; 5267 -0.6; 5793 -2.4; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -8.1; 10263 -6.6; 11289 -6.5; 12418 -6.7; 13660 -17.8; 15026 -28.2; 16529 -29.2; 18182 -25.2; 20000 -21.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Legend X sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Legend X sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.25 | -7.5 dB  |
| Peaking | 159 Hz   | 0.92 | -3.6 dB  |
| Peaking | 4946 Hz  | 0.59 | 15.4 dB  |
| Peaking | 12245 Hz | 1.1  | 21.6 dB  |
| Peaking | 15246 Hz | 0.38 | -35.5 dB |
| Peaking | 873 Hz   | 1    | 7.8 dB   |
| Peaking | 1467 Hz  | 0.43 | -6.4 dB  |
| Peaking | 3066 Hz  | 1.29 | 5.2 dB   |
| Peaking | 4387 Hz  | 8.07 | -1.7 dB  |
| Peaking | 6547 Hz  | 9.03 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 16000 Hz | 1.41 | -28.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Empire%20Ears%20Legend%20X%20sample%201/Empire%20Ears%20Legend%20X%20sample%201.png)