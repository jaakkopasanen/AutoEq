# Etymotic ER4PT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.0; 54 -1.3; 60 -1.7; 66 -2.0; 72 -2.5; 79 -2.9; 87 -3.4; 96 -3.9; 106 -4.2; 116 -4.4; 128 -4.8; 141 -5.2; 155 -5.4; 170 -5.6; 187 -5.7; 206 -5.8; 227 -5.9; 249 -6.0; 274 -6.0; 302 -5.9; 332 -6.0; 365 -5.9; 402 -5.8; 442 -5.7; 486 -5.8; 535 -5.7; 588 -5.4; 647 -5.4; 712 -5.6; 783 -5.6; 861 -6.1; 947 -6.7; 1042 -7.4; 1146 -8.1; 1261 -8.9; 1387 -9.8; 1526 -10.7; 1678 -11.4; 1846 -11.6; 2031 -11.6; 2234 -11.4; 2457 -10.3; 2703 -9.2; 2973 -7.1; 3270 -5.5; 3597 -4.8; 3957 -5.6; 4353 -7.3; 4788 -6.7; 5267 -3.8; 5793 -1.6; 6373 -1.1; 7010 -4.0; 7711 -6.3; 8482 -9.2; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4PT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4PT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.39 | 6.2 dB  |
| Peaking | 1951 Hz | 1.52 | -5.8 dB |
| Peaking | 3440 Hz | 5.16 | 3.0 dB  |
| Peaking | 6171 Hz | 3.62 | 6.3 dB  |
| Peaking | 8609 Hz | 5.55 | -3.6 dB |
| Peaking | 699 Hz  | 1.33 | 1.5 dB  |
| Peaking | 1334 Hz | 2.63 | -1.0 dB |
| Peaking | 4550 Hz | 5.91 | -3.1 dB |
| Peaking | 4716 Hz | 2.53 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20ER4PT/Etymotic%20ER4PT.png)