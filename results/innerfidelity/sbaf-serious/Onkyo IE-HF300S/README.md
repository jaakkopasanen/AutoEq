# Onkyo IE-HF300S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.2; 25 -6.5; 28 -6.9; 31 -7.2; 34 -7.5; 37 -7.8; 41 -8.0; 45 -8.3; 49 -8.6; 54 -8.9; 60 -9.2; 66 -9.5; 72 -9.8; 79 -10.1; 87 -10.5; 96 -10.9; 106 -11.2; 116 -11.2; 128 -11.4; 141 -11.6; 155 -11.6; 170 -11.5; 187 -11.3; 206 -11.2; 227 -10.8; 249 -10.6; 274 -10.2; 302 -9.8; 332 -9.3; 365 -8.7; 402 -8.3; 442 -7.7; 486 -7.2; 535 -6.7; 588 -5.9; 647 -5.6; 712 -5.3; 783 -4.8; 861 -5.0; 947 -5.1; 1042 -5.2; 1146 -5.5; 1261 -5.8; 1387 -6.3; 1526 -6.8; 1678 -7.0; 1846 -6.5; 2031 -5.8; 2234 -4.8; 2457 -3.4; 2703 -2.1; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -1.2; 4353 -4.4; 4788 -6.5; 5267 -6.1; 5793 -4.5; 6373 -2.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Onkyo IE-HF300S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Onkyo IE-HF300S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 86 Hz    | 0.72 | -2.0 dB |
| Peaking | 186 Hz   | 0.6  | -4.2 dB |
| Peaking | 753 Hz   | 1.6  | 2.3 dB  |
| Peaking | 3307 Hz  | 2.02 | 6.7 dB  |
| Peaking | 21899 Hz | 2.34 | 1.4 dB  |
| Peaking | 18 Hz    | 1.94 | 1.0 dB  |
| Peaking | 1753 Hz  | 2.4  | -2.1 dB |
| Peaking | 3309 Hz  | 0.49 | 1.5 dB  |
| Peaking | 5814 Hz  | 1.22 | -4.3 dB |
| Peaking | 6460 Hz  | 3.62 | 7.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Onkyo%20IE-HF300S/Onkyo%20IE-HF300S.png)