# Wiss Audio On Ear Force 1 HP P244
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.9; 25 -10.0; 28 -10.0; 31 -10.1; 34 -10.2; 37 -10.2; 41 -10.3; 45 -10.3; 49 -10.3; 54 -10.2; 60 -10.3; 66 -10.6; 72 -10.8; 79 -11.2; 87 -11.6; 96 -11.8; 106 -11.9; 116 -11.9; 128 -11.9; 141 -11.8; 155 -12.3; 170 -11.8; 187 -12.2; 206 -12.0; 227 -11.4; 249 -10.5; 274 -10.3; 302 -10.8; 332 -11.1; 365 -10.9; 402 -10.2; 442 -9.4; 486 -9.1; 535 -8.7; 588 -7.8; 647 -7.1; 712 -6.6; 783 -6.3; 861 -6.4; 947 -6.5; 1042 -6.5; 1146 -6.4; 1261 -6.2; 1387 -6.5; 1526 -6.6; 1678 -6.7; 1846 -6.2; 2031 -5.2; 2234 -5.0; 2457 -4.5; 2703 -4.5; 2973 -4.7; 3270 -5.1; 3597 -5.0; 3957 -3.7; 4353 -1.7; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Wiss Audio On Ear Force 1 HP P244 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Wiss Audio On Ear Force 1 HP P244 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.98 | -3.0 dB |
| Peaking | 54 Hz   | 0.34 | -3.1 dB |
| Peaking | 164 Hz  | 0.78 | -3.9 dB |
| Peaking | 372 Hz  | 2.18 | -2.6 dB |
| Peaking | 5196 Hz | 1.77 | 6.7 dB  |
| Peaking | 839 Hz  | 1.85 | 1.1 dB  |
| Peaking | 2455 Hz | 2.63 | 1.9 dB  |
| Peaking | 2518 Hz | 0.18 | -0.5 dB |
| Peaking | 6471 Hz | 4.64 | 3.1 dB  |
| Peaking | 7504 Hz | 2.35 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Wiss%20Audio%20On%20Ear%20Force%201%20HP%20P244/Wiss%20Audio%20On%20Ear%20Force%201%20HP%20P244.png)