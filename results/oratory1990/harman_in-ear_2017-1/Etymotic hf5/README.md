# Etymotic hf5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -0.7; 45 -0.9; 49 -1.1; 54 -1.3; 60 -1.6; 66 -2.0; 72 -2.3; 79 -2.7; 87 -3.3; 96 -3.6; 106 -4.4; 116 -4.4; 128 -4.9; 141 -5.5; 155 -5.7; 170 -5.9; 187 -6.1; 206 -6.3; 227 -6.4; 249 -6.5; 274 -6.5; 302 -6.5; 332 -6.4; 365 -6.3; 402 -6.3; 442 -6.3; 486 -6.3; 535 -6.2; 588 -6.0; 647 -5.9; 712 -5.8; 783 -5.7; 861 -5.8; 947 -6.2; 1042 -6.7; 1146 -7.3; 1261 -7.6; 1387 -7.5; 1526 -7.2; 1678 -6.8; 1846 -6.3; 2031 -5.6; 2234 -4.8; 2457 -4.2; 2703 -3.8; 2973 -3.4; 3270 -3.0; 3597 -2.8; 3957 -2.5; 4353 -2.0; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.7; 15026 -22.4; 16529 -19.9; 18182 -8.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic hf5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.48 | 6.4 dB   |
| Peaking | 792 Hz   | 2.57 | 0.9 dB   |
| Peaking | 1341 Hz  | 2.25 | -1.8 dB  |
| Peaking | 4956 Hz  | 0.93 | 5.9 dB   |
| Peaking | 15680 Hz | 2.32 | -18.8 dB |
| Peaking | 4310 Hz  | 5.17 | -1.2 dB  |
| Peaking | 6455 Hz  | 2.37 | 2.9 dB   |
| Peaking | 7590 Hz  | 2.64 | -3.7 dB  |
| Peaking | 12929 Hz | 2.88 | 4.7 dB   |
| Peaking | 14426 Hz | 4.77 | -5.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.8 dB   |
| Peaking | 125 Hz   | 1.41 | 0.8 dB   |
| Peaking | 250 Hz   | 1.41 | -0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 16000 Hz | 1.41 | -15.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Etymotic%20hf5/Etymotic%20hf5.png)