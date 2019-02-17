# Noble PR R Tuning
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -0.9; 66 -1.3; 72 -1.7; 79 -2.1; 87 -2.5; 96 -3.0; 106 -3.4; 116 -3.7; 128 -4.0; 141 -4.3; 155 -4.6; 170 -4.8; 187 -4.9; 206 -5.1; 227 -5.1; 249 -5.2; 274 -5.2; 302 -5.2; 332 -5.2; 365 -5.1; 402 -5.1; 442 -4.9; 486 -4.9; 535 -4.9; 588 -4.7; 647 -4.7; 712 -4.8; 783 -4.9; 861 -5.5; 947 -6.0; 1042 -6.8; 1146 -7.4; 1261 -8.1; 1387 -9.1; 1526 -10.0; 1678 -10.8; 1846 -11.1; 2031 -10.9; 2234 -10.7; 2457 -9.6; 2703 -8.2; 2973 -5.8; 3270 -3.9; 3597 -3.5; 3957 -4.9; 4353 -7.9; 4788 -9.3; 5267 -8.2; 5793 -5.2; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -7.6; 9330 -9.7; 10263 -9.2; 11289 -7.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble PR R Tuning GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble PR R Tuning ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.12 | 6.3 dB  |
| Peaking | 1953 Hz | 1.77 | -5.2 dB |
| Peaking | 3417 Hz | 5.24 | 4.6 dB  |
| Peaking | 6469 Hz | 7.12 | 5.9 dB  |
| Peaking | 9597 Hz | 3.71 | -3.6 dB |
| Peaking | 147 Hz  | 1.36 | -0.8 dB |
| Peaking | 679 Hz  | 0.9  | 2.0 dB  |
| Peaking | 1357 Hz | 1.82 | -1.4 dB |
| Peaking | 4818 Hz | 1.35 | 1.9 dB  |
| Peaking | 4842 Hz | 3.73 | -5.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noble%20PR%20R%20Tuning/Noble%20PR%20R%20Tuning.png)