# Etymotic ER4PT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.7; 60 -1.1; 66 -1.4; 72 -1.9; 79 -2.3; 87 -2.7; 96 -3.2; 106 -3.5; 116 -3.8; 128 -4.2; 141 -4.5; 155 -4.8; 170 -5.0; 187 -5.0; 206 -5.2; 227 -5.2; 249 -5.4; 274 -5.4; 302 -5.3; 332 -5.3; 365 -5.2; 402 -5.2; 442 -5.1; 486 -5.2; 535 -5.1; 588 -4.8; 647 -4.8; 712 -5.0; 783 -5.0; 861 -5.4; 947 -6.0; 1042 -6.8; 1146 -7.5; 1261 -8.2; 1387 -9.2; 1526 -10.1; 1678 -10.7; 1846 -10.9; 2031 -10.9; 2234 -10.8; 2457 -9.7; 2703 -8.6; 2973 -6.5; 3270 -4.8; 3597 -4.2; 3957 -4.9; 4353 -6.7; 4788 -6.1; 5267 -3.2; 5793 -1.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.6; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4PT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4PT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.38 | 6.3 dB  |
| Peaking | 852 Hz  | 0.67 | 5.2 dB  |
| Peaking | 2244 Hz | 0.41 | -8.2 dB |
| Peaking | 3393 Hz | 1.91 | 8.1 dB  |
| Peaking | 6014 Hz | 2.86 | 9.0 dB  |
| Peaking | 8683 Hz | 6.25 | -2.8 dB |
| Peaking | 9931 Hz | 1.32 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20ER4PT/Etymotic%20ER4PT.png)