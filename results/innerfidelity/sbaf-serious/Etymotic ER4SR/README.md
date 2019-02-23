# Etymotic ER4SR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -0.8; 45 -1.1; 49 -1.3; 54 -1.7; 60 -2.0; 66 -2.4; 72 -2.8; 79 -3.2; 87 -3.8; 96 -4.2; 106 -4.5; 116 -4.7; 128 -5.1; 141 -5.4; 155 -5.7; 170 -5.9; 187 -6.0; 206 -6.2; 227 -6.2; 249 -6.2; 274 -6.2; 302 -6.3; 332 -6.2; 365 -6.2; 402 -6.1; 442 -5.9; 486 -6.0; 535 -5.9; 588 -5.7; 647 -5.8; 712 -6.0; 783 -6.1; 861 -6.5; 947 -7.1; 1042 -7.9; 1146 -8.5; 1261 -9.3; 1387 -10.2; 1526 -11.2; 1678 -11.9; 1846 -12.3; 2031 -12.4; 2234 -12.5; 2457 -11.6; 2703 -10.3; 2973 -7.9; 3270 -5.5; 3597 -4.5; 3957 -4.8; 4353 -6.4; 4788 -6.2; 5267 -4.0; 5793 -2.1; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.47 | 6.3 dB  |
| Peaking | 815 Hz   | 0.94 | 2.6 dB  |
| Peaking | 2293 Hz  | 0.62 | -8.0 dB |
| Peaking | 3471 Hz  | 2.17 | 7.5 dB  |
| Peaking | 6117 Hz  | 3    | 7.1 dB  |
| Peaking | 72 Hz    | 2.9  | 0.3 dB  |
| Peaking | 198 Hz   | 1.77 | -0.3 dB |
| Peaking | 12050 Hz | 2.5  | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20ER4SR/Etymotic%20ER4SR.png)