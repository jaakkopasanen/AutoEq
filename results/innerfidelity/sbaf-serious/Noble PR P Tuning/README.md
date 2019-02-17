# Noble PR P Tuning
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -1.7; 25 -1.8; 28 -2.0; 31 -2.2; 34 -2.3; 37 -2.5; 41 -2.7; 45 -2.8; 49 -3.1; 54 -3.4; 60 -3.6; 66 -3.9; 72 -4.3; 79 -4.7; 87 -5.2; 96 -5.6; 106 -5.9; 116 -6.2; 128 -6.5; 141 -6.8; 155 -7.0; 170 -7.2; 187 -7.2; 206 -7.3; 227 -7.3; 249 -7.3; 274 -7.3; 302 -7.1; 332 -7.0; 365 -6.8; 402 -6.7; 442 -6.3; 486 -6.2; 535 -5.9; 588 -5.3; 647 -5.1; 712 -5.0; 783 -4.7; 861 -4.9; 947 -5.1; 1042 -5.3; 1146 -5.4; 1261 -5.6; 1387 -6.1; 1526 -6.4; 1678 -6.7; 1846 -6.5; 2031 -6.3; 2234 -6.3; 2457 -5.9; 2703 -5.1; 2973 -3.0; 3270 -1.0; 3597 -0.5; 3957 -2.8; 4353 -7.2; 4788 -10.1; 5267 -12.3; 5793 -13.9; 6373 -12.4; 7010 -11.4; 7711 -11.8; 8482 -12.7; 9330 -9.5; 10263 -5.4; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.9; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble PR P Tuning GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble PR P Tuning ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.35 | 3.6 dB  |
| Peaking | 193 Hz   | 0.62 | -2.6 dB |
| Peaking | 3572 Hz  | 3.58 | 7.7 dB  |
| Peaking | 5689 Hz  | 1.72 | -8.8 dB |
| Peaking | 8387 Hz  | 4.57 | -5.7 dB |
| Peaking | 802 Hz   | 2.12 | 1.0 dB  |
| Peaking | 1862 Hz  | 1.42 | -1.4 dB |
| Peaking | 3085 Hz  | 7.86 | 1.5 dB  |
| Peaking | 10815 Hz | 4.36 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.3 dB |
| Peaking | 16000 Hz | 1.41 | 1.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noble%20PR%20P%20Tuning/Noble%20PR%20P%20Tuning.png)