# Apple EarPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -1.7; 87 -2.7; 96 -3.4; 106 -3.9; 116 -4.2; 128 -4.4; 141 -4.4; 155 -4.4; 170 -4.3; 187 -4.2; 206 -4.1; 227 -4.0; 249 -4.0; 274 -4.0; 302 -4.0; 332 -3.9; 365 -3.9; 402 -4.1; 442 -4.3; 486 -4.3; 535 -4.4; 588 -4.6; 647 -4.8; 712 -5.0; 783 -5.3; 861 -5.7; 947 -6.2; 1042 -6.8; 1146 -7.5; 1261 -8.4; 1387 -9.5; 1526 -10.9; 1678 -12.3; 1846 -13.2; 2031 -13.2; 2234 -12.8; 2457 -12.3; 2703 -11.9; 2973 -11.2; 3270 -10.2; 3597 -9.4; 3957 -9.0; 4353 -9.3; 4788 -10.4; 5267 -12.4; 5793 -14.2; 6373 -10.8; 7010 -7.5; 7711 -6.9; 8482 -9.1; 9330 -11.1; 10263 -9.9; 11289 -6.7; 12418 -9.0; 13660 -18.5; 15026 -23.5; 16529 -19.7; 18182 -15.7; 20000 -15.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple EarPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple EarPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.03 | 4.1 dB   |
| Peaking | 2104 Hz  | 1.27 | -7.2 dB  |
| Peaking | 5646 Hz  | 4.39 | -6.9 dB  |
| Peaking | 15074 Hz | 2.37 | -14.8 dB |
| Peaking | 18981 Hz | 0.6  | -8.9 dB  |
| Peaking | 106 Hz   | 0.26 | 5.4 dB   |
| Peaking | 144 Hz   | 0.54 | -7.1 dB  |
| Peaking | 7433 Hz  | 3.59 | 4.0 dB   |
| Peaking | 10739 Hz | 0.98 | -5.4 dB  |
| Peaking | 11735 Hz | 3.11 | 9.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 5.0 dB   |
| Peaking | 125 Hz   | 1.41 | 0.7 dB   |
| Peaking | 250 Hz   | 1.41 | 2.0 dB   |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -18.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Apple%20EarPods/Apple%20EarPods.png)