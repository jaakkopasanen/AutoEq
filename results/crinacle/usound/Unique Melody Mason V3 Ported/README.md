# Unique Melody Mason V3 Ported
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.9; 37 -1.4; 41 -2.1; 45 -2.7; 49 -3.2; 54 -3.8; 60 -4.4; 66 -5.0; 72 -5.5; 79 -6.0; 87 -6.5; 96 -7.1; 106 -7.5; 116 -7.8; 128 -8.0; 141 -8.2; 155 -8.3; 170 -8.3; 187 -8.3; 206 -8.2; 227 -8.0; 249 -7.8; 274 -7.5; 302 -7.2; 332 -7.1; 365 -6.9; 402 -6.7; 442 -6.5; 486 -6.4; 535 -6.3; 588 -6.2; 647 -6.1; 712 -6.0; 783 -5.9; 861 -5.9; 947 -6.1; 1042 -6.6; 1146 -7.4; 1261 -8.2; 1387 -8.7; 1526 -8.5; 1678 -8.0; 1846 -7.3; 2031 -6.8; 2234 -6.2; 2457 -5.3; 2703 -4.0; 2973 -2.9; 3270 -2.8; 3597 -1.7; 3957 -0.5; 4353 -0.9; 4788 -4.5; 5267 -9.5; 5793 -11.4; 6373 -8.0; 7010 -8.4; 7711 -8.9; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -8.1; 18182 -9.5; 20000 -11.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody Mason V3 Ported GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody Mason V3 Ported ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 26 Hz    |  0.66 | 6.4 dB   |
| Peaking | 145 Hz   |  0.91 | -2.4 dB  |
| Peaking | 1519 Hz  |  2.48 | -2.9 dB  |
| Peaking | 4335 Hz  |  1.51 | 11.2 dB  |
| Peaking | 5456 Hz  |  1.99 | -11.0 dB |
| Peaking | 803 Hz   |  1.55 | 0.9 dB   |
| Peaking | 1232 Hz  |  4.87 | -0.9 dB  |
| Peaking | 6495 Hz  | 14.81 | 1.9 dB   |
| Peaking | 14578 Hz |  1.18 | 1.5 dB   |
| Peaking | 19757 Hz |  0.41 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Unique%20Melody%20Mason%20V3%20Ported/Unique%20Melody%20Mason%20V3%20Ported.png)