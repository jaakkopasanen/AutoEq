# Apple EarPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -1.3; 79 -2.6; 87 -3.8; 96 -4.9; 106 -5.5; 116 -5.9; 128 -6.2; 141 -6.2; 155 -6.2; 170 -6.1; 187 -5.9; 206 -5.8; 227 -5.4; 249 -5.4; 274 -5.2; 302 -5.1; 332 -5.0; 365 -4.8; 402 -4.7; 442 -4.5; 486 -4.8; 535 -4.8; 588 -4.5; 647 -4.7; 712 -5.0; 783 -5.2; 861 -5.6; 947 -6.1; 1042 -6.8; 1146 -7.5; 1261 -8.7; 1387 -10.5; 1526 -12.7; 1678 -14.7; 1846 -16.2; 2031 -17.0; 2234 -17.2; 2457 -16.4; 2703 -15.4; 2973 -12.8; 3270 -9.9; 3597 -8.0; 3957 -8.0; 4353 -10.0; 4788 -11.1; 5267 -11.7; 5793 -14.2; 6373 -13.4; 7010 -11.9; 7711 -12.2; 8482 -13.7; 9330 -14.8; 10263 -12.4; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -7.8; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple EarPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple EarPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.66 | 6.9 dB   |
| Peaking | 657 Hz   | 0.75 | 2.6 dB   |
| Peaking | 2070 Hz  | 1.51 | -11.6 dB |
| Peaking | 7792 Hz  | 1.14 | -7.1 dB  |
| Peaking | 22050 Hz | 2.3  | -5.9 dB  |
| Peaking | 67 Hz    | 5.77 | 2.0 dB   |
| Peaking | 3702 Hz  | 7.24 | 3.1 dB   |
| Peaking | 5798 Hz  | 4.62 | -3.9 dB  |
| Peaking | 9618 Hz  | 3.33 | -9.0 dB  |
| Peaking | 9716 Hz  | 1.21 | 5.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 5.1 dB   |
| Peaking | 125 Hz   | 1.41 | -1.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.8 dB   |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -7.8 dB  |
| Peaking | 16000 Hz | 1.41 | 0.4 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20EarPods/Apple%20EarPods.png)