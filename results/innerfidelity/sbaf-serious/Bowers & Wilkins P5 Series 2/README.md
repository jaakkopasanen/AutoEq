# Bowers & Wilkins P5 Series 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -12.1; 25 -12.5; 28 -13.0; 31 -13.3; 34 -13.6; 37 -13.7; 41 -13.9; 45 -14.0; 49 -14.2; 54 -14.3; 60 -14.4; 66 -14.6; 72 -14.6; 79 -14.8; 87 -14.9; 96 -15.0; 106 -14.9; 116 -14.9; 128 -14.8; 141 -14.6; 155 -14.5; 170 -14.0; 187 -13.7; 206 -13.3; 227 -12.7; 249 -11.7; 274 -10.4; 302 -9.3; 332 -8.6; 365 -7.0; 402 -5.4; 442 -3.7; 486 -2.3; 535 -1.2; 588 -0.5; 647 -0.7; 712 -1.5; 783 -2.1; 861 -3.2; 947 -4.2; 1042 -5.3; 1146 -6.4; 1261 -7.8; 1387 -9.3; 1526 -10.9; 1678 -11.6; 1846 -11.9; 2031 -11.6; 2234 -11.2; 2457 -10.0; 2703 -7.9; 2973 -6.0; 3270 -5.4; 3597 -5.0; 3957 -6.5; 4353 -8.2; 4788 -8.5; 5267 -7.7; 5793 -6.7; 6373 -5.2; 7010 -2.7; 7711 -4.6; 8482 -4.9; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -5.0; 18182 -6.4; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Series 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Series 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.3  | -7.5 dB |
| Peaking | 199 Hz   | 0.44 | -7.3 dB |
| Peaking | 581 Hz   | 0.95 | 8.6 dB  |
| Peaking | 1796 Hz  | 1.25 | -7.9 dB |
| Peaking | 2382 Hz  | 5    | -1.7 dB |
| Peaking | 3512 Hz  | 1.79 | 3.9 dB  |
| Peaking | 4568 Hz  | 1.96 | -4.8 dB |
| Peaking | 6981 Hz  | 6.08 | 3.1 dB  |
| Peaking | 18796 Hz | 1.64 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | -7.2 dB |
| Peaking | 125 Hz   | 1.41 | -8.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.8 dB |
| Peaking | 500 Hz   | 1.41 | 5.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P5%20Series%202/Bowers%20&%20Wilkins%20P5%20Series%202.png)