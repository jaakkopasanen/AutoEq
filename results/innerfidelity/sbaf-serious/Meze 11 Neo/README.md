# Meze 11 Neo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.2; 25 -2.7; 28 -3.4; 31 -4.0; 34 -4.5; 37 -4.9; 41 -5.5; 45 -6.0; 49 -6.4; 54 -6.9; 60 -7.4; 66 -7.9; 72 -8.4; 79 -8.8; 87 -9.4; 96 -9.9; 106 -10.2; 116 -10.3; 128 -10.7; 141 -10.9; 155 -11.0; 170 -11.0; 187 -10.9; 206 -10.9; 227 -10.6; 249 -10.4; 274 -10.0; 302 -9.6; 332 -9.2; 365 -8.7; 402 -8.2; 442 -7.5; 486 -7.0; 535 -6.4; 588 -5.5; 647 -5.0; 712 -4.5; 783 -4.2; 861 -4.1; 947 -4.3; 1042 -4.6; 1146 -4.8; 1261 -5.2; 1387 -5.8; 1526 -6.5; 1678 -7.0; 1846 -7.4; 2031 -7.7; 2234 -7.9; 2457 -7.2; 2703 -6.1; 2973 -3.9; 3270 -2.0; 3597 -1.0; 3957 -1.6; 4353 -3.8; 4788 -4.5; 5267 -3.2; 5793 -1.7; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 11 Neo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 11 Neo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.21 | 4.5 dB  |
| Peaking | 157 Hz  | 0.67 | -5.6 dB |
| Peaking | 2241 Hz | 3.1  | -2.8 dB |
| Peaking | 3572 Hz | 2.86 | 5.3 dB  |
| Peaking | 6217 Hz | 4.44 | 5.5 dB  |
| Peaking | 162 Hz  | 1.22 | 1.7 dB  |
| Peaking | 357 Hz  | 0.35 | -2.0 dB |
| Peaking | 786 Hz  | 0.9  | 3.8 dB  |
| Peaking | 1685 Hz | 3.2  | -1.2 dB |
| Peaking | 8173 Hz | 4.67 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2011%20Neo/Meze%2011%20Neo.png)