# Monster Beats Studio
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -3.4; 28 -7.8; 31 -11.3; 34 -12.9; 37 -13.3; 41 -13.2; 45 -12.8; 49 -12.6; 54 -12.4; 60 -12.2; 66 -12.0; 72 -11.8; 79 -12.1; 87 -12.8; 96 -13.4; 106 -13.7; 116 -13.8; 128 -14.0; 141 -14.2; 155 -14.1; 170 -14.1; 187 -14.2; 206 -14.1; 227 -14.0; 249 -13.9; 274 -13.6; 302 -13.5; 332 -13.4; 365 -12.8; 402 -13.0; 442 -12.7; 486 -12.3; 535 -11.8; 588 -10.6; 647 -8.7; 712 -7.4; 783 -6.1; 861 -5.5; 947 -5.9; 1042 -6.9; 1146 -8.3; 1261 -10.2; 1387 -11.9; 1526 -12.9; 1678 -13.8; 1846 -13.6; 2031 -12.8; 2234 -11.7; 2457 -10.1; 2703 -8.4; 2973 -6.4; 3270 -4.3; 3597 -6.3; 3957 -7.5; 4353 -10.2; 4788 -12.0; 5267 -7.3; 5793 -9.6; 6373 -7.9; 7010 -8.4; 7711 -12.0; 8482 -15.6; 9330 -15.4; 10263 -11.4; 11289 -6.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Studio GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Studio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 1.68 | 12.5 dB  |
| Peaking | 34 Hz   | 1    | -9.1 dB  |
| Peaking | 194 Hz  | 0.47 | -7.9 dB  |
| Peaking | 1790 Hz | 2.32 | -7.6 dB  |
| Peaking | 8832 Hz | 2.85 | -10.1 dB |
| Peaking | 504 Hz  | 2.07 | -2.6 dB  |
| Peaking | 850 Hz  | 1.89 | 3.9 dB   |
| Peaking | 1358 Hz | 3.77 | -2.3 dB  |
| Peaking | 3305 Hz | 7.31 | 3.9 dB   |
| Peaking | 4624 Hz | 8.76 | -6.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -6.3 dB |
| Peaking | 500 Hz   | 1.41 | -4.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Studio/Monster%20Beats%20Studio.png)