# Pioneer Monitor 10 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.0; 25 -11.1; 28 -11.2; 31 -11.2; 34 -11.2; 37 -11.2; 41 -11.2; 45 -11.3; 49 -11.4; 54 -11.5; 60 -11.5; 66 -11.6; 72 -11.5; 79 -11.4; 87 -11.3; 96 -11.3; 106 -11.6; 116 -11.6; 128 -10.5; 141 -9.5; 155 -13.0; 170 -10.7; 187 -10.9; 206 -12.1; 227 -12.7; 249 -13.0; 274 -13.0; 302 -12.3; 332 -12.1; 365 -11.0; 402 -9.8; 442 -8.3; 486 -7.2; 535 -5.7; 588 -3.8; 647 -2.8; 712 -2.5; 783 -3.5; 861 -5.0; 947 -6.5; 1042 -6.3; 1146 -6.7; 1261 -8.0; 1387 -10.8; 1526 -14.1; 1678 -15.8; 1846 -14.2; 2031 -10.5; 2234 -7.3; 2457 -6.4; 2703 -6.8; 2973 -4.4; 3270 -3.0; 3597 -3.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer Monitor 10 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer Monitor 10 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.39 | -4.7 dB  |
| Peaking | 126 Hz  | 0.92 | -2.5 dB  |
| Peaking | 270 Hz  | 2.03 | -6.0 dB  |
| Peaking | 1697 Hz | 3.66 | -10.9 dB |
| Peaking | 4676 Hz | 1.3  | 6.6 dB   |
| Peaking | 376 Hz  | 3.52 | -1.9 dB  |
| Peaking | 637 Hz  | 2.93 | 3.9 dB   |
| Peaking | 760 Hz  | 4.44 | 2.4 dB   |
| Peaking | 6360 Hz | 3.88 | 4.7 dB   |
| Peaking | 7114 Hz | 1.48 | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -7.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20Monitor%2010%20II/Pioneer%20Monitor%2010%20II.png)