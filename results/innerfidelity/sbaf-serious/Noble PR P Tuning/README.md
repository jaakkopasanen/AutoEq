# Noble PR P Tuning
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.4; 25 -1.5; 28 -1.7; 31 -1.8; 34 -2.0; 37 -2.2; 41 -2.3; 45 -2.5; 49 -2.8; 54 -3.0; 60 -3.3; 66 -3.6; 72 -4.0; 79 -4.4; 87 -4.9; 96 -5.3; 106 -5.6; 116 -5.8; 128 -6.2; 141 -6.5; 155 -6.7; 170 -6.9; 187 -6.9; 206 -7.0; 227 -7.0; 249 -6.9; 274 -6.9; 302 -6.8; 332 -6.7; 365 -6.5; 402 -6.4; 442 -6.0; 486 -5.9; 535 -5.6; 588 -5.0; 647 -4.8; 712 -4.7; 783 -4.4; 861 -4.6; 947 -4.8; 1042 -5.0; 1146 -5.0; 1261 -5.3; 1387 -5.7; 1526 -6.1; 1678 -6.4; 1846 -6.2; 2031 -6.0; 2234 -6.0; 2457 -5.5; 2703 -4.8; 2973 -2.7; 3270 -0.8; 3597 -0.5; 3957 -2.5; 4353 -6.9; 4788 -9.8; 5267 -12.0; 5793 -13.6; 6373 -12.1; 7010 -11.1; 7711 -11.5; 8482 -12.4; 9330 -9.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble PR P Tuning GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble PR P Tuning ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.83 | 5.0 dB  |
| Peaking | 55 Hz    | 1.39 | 2.2 dB  |
| Peaking | 3540 Hz  | 2.44 | 8.1 dB  |
| Peaking | 5621 Hz  | 1.99 | -7.9 dB |
| Peaking | 8334 Hz  | 4.87 | -4.9 dB |
| Peaking | 242 Hz   | 1.07 | -0.9 dB |
| Peaking | 823 Hz   | 0.97 | 2.1 dB  |
| Peaking | 1945 Hz  | 1.28 | -0.7 dB |
| Peaking | 10384 Hz | 5.33 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.8 dB |
| Peaking | 16000 Hz | 1.41 | 1.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noble%20PR%20P%20Tuning/Noble%20PR%20P%20Tuning.png)