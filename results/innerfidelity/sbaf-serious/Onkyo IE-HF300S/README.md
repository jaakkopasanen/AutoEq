# Onkyo IE-HF300S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.3; 25 -7.6; 28 -8.0; 31 -8.3; 34 -8.6; 37 -8.8; 41 -9.1; 45 -9.4; 49 -9.6; 54 -9.9; 60 -10.3; 66 -10.6; 72 -10.9; 79 -11.2; 87 -11.6; 96 -12.0; 106 -12.2; 116 -12.3; 128 -12.5; 141 -12.6; 155 -12.6; 170 -12.6; 187 -12.4; 206 -12.2; 227 -11.9; 249 -11.6; 274 -11.2; 302 -10.8; 332 -10.3; 365 -9.8; 402 -9.4; 442 -8.7; 486 -8.3; 535 -7.8; 588 -7.0; 647 -6.6; 712 -6.4; 783 -5.9; 861 -6.0; 947 -6.1; 1042 -6.3; 1146 -6.5; 1261 -6.8; 1387 -7.4; 1526 -7.8; 1678 -8.0; 1846 -7.6; 2031 -6.8; 2234 -5.8; 2457 -4.4; 2703 -3.1; 2973 -1.7; 3270 -0.5; 3597 -0.6; 3957 -2.3; 4353 -5.5; 4788 -7.5; 5267 -7.1; 5793 -5.6; 6373 -3.5; 7010 -3.8; 7711 -6.0; 8482 -6.9; 9330 -7.6; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Onkyo IE-HF300S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Onkyo IE-HF300S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 103 Hz   | 0.49 | -5.1 dB |
| Peaking | 236 Hz   | 0.95 | -3.0 dB |
| Peaking | 1699 Hz  | 3.34 | -2.3 dB |
| Peaking | 3297 Hz  | 2.72 | 6.5 dB  |
| Peaking | 22050 Hz | 2.17 | 0.9 dB  |
| Peaking | 796 Hz   | 2.99 | 1.1 dB  |
| Peaking | 3928 Hz  | 6.43 | 2.0 dB  |
| Peaking | 4879 Hz  | 3.18 | -2.9 dB |
| Peaking | 6624 Hz  | 4.84 | 3.7 dB  |
| Peaking | 9023 Hz  | 6.79 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Onkyo%20IE-HF300S/Onkyo%20IE-HF300S.png)