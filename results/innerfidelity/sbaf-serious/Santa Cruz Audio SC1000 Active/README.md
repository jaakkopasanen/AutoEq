# Santa Cruz Audio SC1000 Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.0; 25 -1.1; 28 -1.3; 31 -1.4; 34 -1.6; 37 -1.7; 41 -1.9; 45 -2.1; 49 -2.2; 54 -2.4; 60 -2.8; 66 -3.2; 72 -3.6; 79 -3.9; 87 -4.2; 96 -4.6; 106 -4.9; 116 -5.1; 128 -5.5; 141 -5.8; 155 -5.9; 170 -6.1; 187 -6.2; 206 -6.2; 227 -6.2; 249 -6.2; 274 -6.3; 302 -6.2; 332 -6.2; 365 -6.2; 402 -6.1; 442 -5.8; 486 -5.8; 535 -5.8; 588 -5.4; 647 -5.4; 712 -5.7; 783 -5.6; 861 -6.0; 947 -6.4; 1042 -6.4; 1146 -6.5; 1261 -6.6; 1387 -7.2; 1526 -7.8; 1678 -8.2; 1846 -8.3; 2031 -8.2; 2234 -8.4; 2457 -8.3; 2703 -8.7; 2973 -7.9; 3270 -6.0; 3597 -4.4; 3957 -4.6; 4353 -7.3; 4788 -9.1; 5267 -4.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -7.9; 9330 -8.6; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Santa Cruz Audio SC1000 Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Santa Cruz Audio SC1000 Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 0.63 | 5.0 dB   |
| Peaking | 52 Hz   | 0.7  | 2.7 dB   |
| Peaking | 3772 Hz | 2.88 | 9.2 dB   |
| Peaking | 4587 Hz | 0.96 | -10.3 dB |
| Peaking | 5932 Hz | 2.56 | 13.5 dB  |
| Peaking | 657 Hz  | 1.65 | 1.2 dB   |
| Peaking | 1240 Hz | 3.56 | 0.6 dB   |
| Peaking | 1661 Hz | 2.43 | -0.8 dB  |
| Peaking | 9132 Hz | 4.12 | -3.1 dB  |
| Peaking | 9837 Hz | 1.29 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Santa%20Cruz%20Audio%20SC1000%20Active/Santa%20Cruz%20Audio%20SC1000%20Active.png)