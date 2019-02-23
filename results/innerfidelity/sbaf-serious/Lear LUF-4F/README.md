# Lear LUF-4F
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -4.9; 25 -5.1; 28 -5.4; 31 -5.7; 34 -5.9; 37 -6.1; 41 -6.4; 45 -6.7; 49 -6.9; 54 -7.2; 60 -7.6; 66 -7.9; 72 -8.2; 79 -8.5; 87 -8.8; 96 -9.1; 106 -9.2; 116 -9.1; 128 -9.1; 141 -8.8; 155 -8.5; 170 -8.0; 187 -7.3; 206 -6.7; 227 -5.9; 249 -5.4; 274 -4.9; 302 -4.5; 332 -4.3; 365 -4.1; 402 -4.1; 442 -4.0; 486 -4.1; 535 -4.1; 588 -3.9; 647 -4.0; 712 -4.3; 783 -4.3; 861 -4.8; 947 -5.4; 1042 -6.2; 1146 -7.0; 1261 -7.9; 1387 -9.2; 1526 -10.7; 1678 -11.7; 1846 -12.3; 2031 -12.5; 2234 -12.4; 2457 -11.2; 2703 -9.3; 2973 -6.6; 3270 -5.6; 3597 -6.2; 3957 -4.9; 4353 -0.8; 4788 -0.5; 5267 -4.9; 5793 -5.6; 6373 -4.0; 7010 -4.5; 7711 -8.3; 8482 -9.6; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lear LUF-4F GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lear LUF-4F ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 108 Hz  |  0.53 | -7.2 dB  |
| Peaking | 398 Hz  |  0.06 | 4.6 dB   |
| Peaking | 1918 Hz |  1.07 | -10.7 dB |
| Peaking | 4577 Hz |  5.11 | 5.7 dB   |
| Peaking | 8271 Hz |  5.95 | -5.0 dB  |
| Peaking | 12 Hz   |  2.12 | 0.7 dB   |
| Peaking | 2429 Hz |  6.56 | -1.1 dB  |
| Peaking | 3083 Hz |  8.32 | 1.9 dB   |
| Peaking | 5574 Hz | 10.85 | -2.2 dB  |
| Peaking | 6641 Hz |  7.3  | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Lear%20LUF-4F/Lear%20LUF-4F.png)