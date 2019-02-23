# Apple EarPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.5; 96 -2.6; 106 -3.2; 116 -3.5; 128 -3.8; 141 -3.9; 155 -3.9; 170 -3.7; 187 -3.6; 206 -3.4; 227 -3.1; 249 -3.1; 274 -2.8; 302 -2.8; 332 -2.6; 365 -2.4; 402 -2.4; 442 -2.2; 486 -2.4; 535 -2.4; 588 -2.2; 647 -2.4; 712 -2.7; 783 -2.8; 861 -3.3; 947 -3.8; 1042 -4.4; 1146 -5.2; 1261 -6.4; 1387 -8.2; 1526 -10.3; 1678 -12.4; 1846 -13.9; 2031 -14.7; 2234 -14.9; 2457 -14.1; 2703 -13.1; 2973 -10.4; 3270 -7.6; 3597 -5.6; 3957 -5.7; 4353 -7.7; 4788 -8.7; 5267 -9.3; 5793 -11.9; 6373 -11.1; 7010 -9.6; 7711 -9.9; 8482 -11.4; 9330 -12.4; 10263 -10.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple EarPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple EarPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.42 | 6.5 dB   |
| Peaking | 620 Hz   | 0.44 | 4.6 dB   |
| Peaking | 2035 Hz  | 1.64 | -10.7 dB |
| Peaking | 8121 Hz  | 1.37 | -4.8 dB  |
| Peaking | 22050 Hz | 2.12 | -3.8 dB  |
| Peaking | 2708 Hz  | 5.18 | -2.6 dB  |
| Peaking | 3679 Hz  | 3.44 | 3.9 dB   |
| Peaking | 6039 Hz  | 2.7  | -3.4 dB  |
| Peaking | 7129 Hz  | 4.96 | 3.1 dB   |
| Peaking | 11748 Hz | 5.04 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20EarPods/Apple%20EarPods.png)