# Shozy x AAW Hibiki SE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.4; 25 -11.6; 28 -11.7; 31 -11.8; 34 -11.8; 37 -11.8; 41 -11.8; 45 -11.7; 49 -11.7; 54 -11.7; 60 -11.6; 66 -11.6; 72 -11.6; 79 -11.7; 87 -11.7; 96 -11.7; 106 -11.9; 116 -11.8; 128 -11.8; 141 -11.8; 155 -11.7; 170 -11.5; 187 -11.3; 206 -11.0; 227 -10.7; 249 -10.4; 274 -10.0; 302 -9.5; 332 -8.9; 365 -8.4; 402 -7.9; 442 -7.4; 486 -6.9; 535 -6.5; 588 -6.0; 647 -5.5; 712 -5.1; 783 -4.4; 861 -3.7; 947 -3.6; 1042 -4.0; 1146 -4.8; 1261 -5.4; 1387 -5.8; 1526 -6.0; 1678 -6.3; 1846 -6.9; 2031 -7.5; 2234 -7.8; 2457 -7.1; 2703 -5.7; 2973 -4.5; 3270 -4.6; 3597 -6.5; 3957 -8.3; 4353 -5.9; 4788 -1.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.9; 15026 -17.4; 16529 -18.2; 18182 -15.2; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shozy x AAW Hibiki SE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shozy x AAW Hibiki SE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 64 Hz    | 0.18 | -5.5 dB  |
| Peaking | 832 Hz   | 1.33 | 3.6 dB   |
| Peaking | 5064 Hz  | 6.81 | 4.5 dB   |
| Peaking | 6104 Hz  | 3.26 | 6.1 dB   |
| Peaking | 16875 Hz | 1.25 | -13.0 dB |
| Peaking | 2288 Hz  | 2.58 | -2.9 dB  |
| Peaking | 3064 Hz  | 1.84 | 3.0 dB   |
| Peaking | 3927 Hz  | 5.46 | -4.1 dB  |
| Peaking | 13383 Hz | 2.07 | 5.3 dB   |
| Peaking | 14891 Hz | 3.21 | -6.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 16000 Hz | 1.41 | -13.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shozy%20x%20AAW%20Hibiki%20SE/Shozy%20x%20AAW%20Hibiki%20SE.png)