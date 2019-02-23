# Noble PR R Tuning
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -0.9; 60 -1.4; 66 -1.7; 72 -2.1; 79 -2.5; 87 -2.9; 96 -3.4; 106 -3.8; 116 -4.1; 128 -4.4; 141 -4.7; 155 -5.0; 170 -5.2; 187 -5.3; 206 -5.5; 227 -5.5; 249 -5.6; 274 -5.6; 302 -5.6; 332 -5.6; 365 -5.5; 402 -5.5; 442 -5.3; 486 -5.3; 535 -5.3; 588 -5.1; 647 -5.1; 712 -5.3; 783 -5.3; 861 -5.9; 947 -6.5; 1042 -7.2; 1146 -7.8; 1261 -8.6; 1387 -9.5; 1526 -10.4; 1678 -11.2; 1846 -11.5; 2031 -11.3; 2234 -11.1; 2457 -10.0; 2703 -8.6; 2973 -6.2; 3270 -4.4; 3597 -4.0; 3957 -5.3; 4353 -8.3; 4788 -9.7; 5267 -8.6; 5793 -5.6; 6373 -1.9; 7010 -4.0; 7711 -6.2; 8482 -8.0; 9330 -10.1; 10263 -9.6; 11289 -7.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble PR R Tuning GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble PR R Tuning ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.41 | 6.4 dB   |
| Peaking | 1953 Hz  | 0.83 | -15.1 dB |
| Peaking | 3030 Hz  | 0.3  | 10.5 dB  |
| Peaking | 4834 Hz  | 3.58 | -8.6 dB  |
| Peaking | 9618 Hz  | 1.84 | -7.9 dB  |
| Peaking | 1977 Hz  | 4.28 | 1.6 dB   |
| Peaking | 2754 Hz  | 1.45 | -1.6 dB  |
| Peaking | 3285 Hz  | 4.5  | 2.3 dB   |
| Peaking | 12212 Hz | 0.85 | 0.9 dB   |
| Peaking | 14135 Hz | 1.03 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noble%20PR%20R%20Tuning/Noble%20PR%20R%20Tuning.png)