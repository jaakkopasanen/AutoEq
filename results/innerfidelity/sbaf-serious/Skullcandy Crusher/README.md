# Skullcandy Crusher
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -2.0; 25 -3.3; 28 -5.0; 31 -6.4; 34 -7.6; 37 -8.6; 41 -9.6; 45 -10.2; 49 -10.5; 54 -10.6; 60 -10.9; 66 -10.9; 72 -10.6; 79 -10.2; 87 -9.6; 96 -8.5; 106 -9.2; 116 -9.8; 128 -10.6; 141 -10.3; 155 -10.7; 170 -10.2; 187 -10.7; 206 -10.8; 227 -10.9; 249 -11.0; 274 -10.9; 302 -11.0; 332 -10.6; 365 -10.2; 402 -10.0; 442 -10.0; 486 -10.0; 535 -10.3; 588 -10.1; 647 -10.1; 712 -10.0; 783 -9.5; 861 -9.1; 947 -7.9; 1042 -6.4; 1146 -4.6; 1261 -5.5; 1387 -5.9; 1526 -7.8; 1678 -9.0; 1846 -8.9; 2031 -9.2; 2234 -8.3; 2457 -8.3; 2703 -7.5; 2973 -6.8; 3270 -7.3; 3597 -6.9; 3957 -7.8; 4353 -8.6; 4788 -2.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Crusher GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.61 | 7.4 dB  |
| Peaking | 51 Hz   | 1.11 | -4.3 dB |
| Peaking | 253 Hz  | 0.48 | -4.3 dB |
| Peaking | 675 Hz  | 2.82 | -1.8 dB |
| Peaking | 5762 Hz | 3.67 | 7.2 dB  |
| Peaking | 20 Hz   | 0.78 | 0.3 dB  |
| Peaking | 1224 Hz | 3.35 | 3.9 dB  |
| Peaking | 1841 Hz | 1.43 | -2.7 dB |
| Peaking | 4226 Hz | 7.64 | -4.3 dB |
| Peaking | 4918 Hz | 8.69 | 3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Crusher/Skullcandy%20Crusher.png)