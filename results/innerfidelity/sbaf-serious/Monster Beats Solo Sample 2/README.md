# Monster Beats Solo sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.7; 25 -3.3; 28 -4.1; 31 -4.8; 34 -5.3; 37 -5.9; 41 -6.7; 45 -6.8; 49 -6.4; 54 -6.5; 60 -7.2; 66 -7.8; 72 -8.8; 79 -10.5; 87 -12.0; 96 -13.1; 106 -14.1; 116 -14.7; 128 -15.0; 141 -15.3; 155 -15.4; 170 -15.4; 187 -15.1; 206 -14.1; 227 -13.9; 249 -14.6; 274 -14.4; 302 -12.4; 332 -10.0; 365 -7.8; 402 -7.0; 442 -6.1; 486 -5.6; 535 -6.2; 588 -6.8; 647 -7.8; 712 -8.6; 783 -9.0; 861 -9.3; 947 -9.3; 1042 -9.0; 1146 -8.6; 1261 -8.3; 1387 -8.3; 1526 -7.9; 1678 -7.2; 1846 -6.1; 2031 -4.8; 2234 -4.1; 2457 -2.9; 2703 -2.7; 2973 -2.1; 3270 -2.1; 3597 -2.2; 3957 -3.5; 4353 -6.3; 4788 -4.5; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Solo sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Solo sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 12 Hz   |  0.47 | 5.6 dB  |
| Peaking | 139 Hz  |  0.9  | -9.5 dB |
| Peaking | 262 Hz  |  3.73 | -4.8 dB |
| Peaking | 3036 Hz |  2.42 | 4.8 dB  |
| Peaking | 5860 Hz |  3.59 | 6.5 dB  |
| Peaking | 60 Hz   |  4.29 | 1.2 dB  |
| Peaking | 487 Hz  |  1.45 | 5.5 dB  |
| Peaking | 714 Hz  |  0.58 | -4.1 dB |
| Peaking | 2230 Hz |  2.43 | 2.1 dB  |
| Peaking | 4462 Hz | 14.6  | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -8.4 dB |
| Peaking | 250 Hz   | 1.41 | -7.0 dB |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Solo%20sample%202/Monster%20Beats%20Solo%20sample%202.png)