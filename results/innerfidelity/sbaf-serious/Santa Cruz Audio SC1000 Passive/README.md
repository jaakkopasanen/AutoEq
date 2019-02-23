# Santa Cruz Audio SC1000 Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.7; 106 -1.0; 116 -1.1; 128 -1.5; 141 -1.8; 155 -2.0; 170 -2.1; 187 -2.2; 206 -2.3; 227 -2.3; 249 -2.3; 274 -2.4; 302 -2.4; 332 -2.4; 365 -2.4; 402 -2.3; 442 -2.1; 486 -2.2; 535 -2.2; 588 -2.0; 647 -2.1; 712 -2.3; 783 -2.4; 861 -3.0; 947 -3.6; 1042 -3.9; 1146 -4.1; 1261 -4.6; 1387 -5.4; 1526 -6.4; 1678 -7.3; 1846 -7.9; 2031 -8.4; 2234 -9.1; 2457 -9.8; 2703 -10.9; 2973 -11.0; 3270 -10.3; 3597 -9.7; 3957 -11.3; 4353 -15.5; 4788 -19.0; 5267 -17.0; 5793 -12.8; 6373 -11.1; 7010 -12.7; 7711 -16.2; 8482 -18.0; 9330 -16.5; 10263 -12.6; 11289 -7.1; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Santa Cruz Audio SC1000 Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Santa Cruz Audio SC1000 Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.12 | 6.0 dB   |
| Peaking | 641 Hz   | 1.02 | 3.8 dB   |
| Peaking | 4785 Hz  | 1.91 | -10.9 dB |
| Peaking | 8686 Hz  | 3    | -11.2 dB |
| Peaking | 22050 Hz | 2.2  | -9.5 dB  |
| Peaking | 1168 Hz  | 2.76 | 1.2 dB   |
| Peaking | 2836 Hz  | 1.4  | -3.6 dB  |
| Peaking | 3667 Hz  | 2.83 | 2.0 dB   |
| Peaking | 3720 Hz  | 3.31 | 2.1 dB   |
| Peaking | 11287 Hz | 2.56 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 3.9 dB  |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | -5.9 dB |
| Peaking | 8000 Hz  | 1.41 | -9.5 dB |
| Peaking | 16000 Hz | 1.41 | 1.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Santa%20Cruz%20Audio%20SC1000%20Passive/Santa%20Cruz%20Audio%20SC1000%20Passive.png)