# Bowers & Wilkins P5 Series 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -11.0; 25 -11.4; 28 -11.9; 31 -12.3; 34 -12.5; 37 -12.7; 41 -12.8; 45 -13.0; 49 -13.1; 54 -13.3; 60 -13.4; 66 -13.6; 72 -13.6; 79 -13.8; 87 -13.9; 96 -14.0; 106 -13.9; 116 -13.9; 128 -13.8; 141 -13.5; 155 -13.4; 170 -13.0; 187 -12.7; 206 -12.3; 227 -11.6; 249 -10.7; 274 -9.3; 302 -8.3; 332 -7.6; 365 -6.0; 402 -4.3; 442 -2.7; 486 -1.3; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -1.1; 861 -2.1; 947 -3.2; 1042 -4.3; 1146 -5.4; 1261 -6.7; 1387 -8.2; 1526 -9.9; 1678 -10.5; 1846 -10.9; 2031 -10.5; 2234 -10.1; 2457 -9.0; 2703 -6.9; 2973 -5.0; 3270 -4.3; 3597 -4.0; 3957 -5.5; 4353 -7.2; 4788 -7.4; 5267 -6.6; 5793 -5.7; 6373 -4.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Series 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Series 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 171 Hz  | 0.12 | -7.5 dB  |
| Peaking | 287 Hz  | 0.34 | -11.0 dB |
| Peaking | 542 Hz  | 0.38 | 22.3 dB  |
| Peaking | 1771 Hz | 1.23 | -9.7 dB  |
| Peaking | 2391 Hz | 5.26 | -1.9 dB  |
| Peaking | 3538 Hz | 2.09 | 3.3 dB   |
| Peaking | 4462 Hz | 2.48 | -3.5 dB  |
| Peaking | 6681 Hz | 4.72 | 3.9 dB   |
| Peaking | 7410 Hz | 1.57 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | 7.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P5%20Series%202/Bowers%20&%20Wilkins%20P5%20Series%202.png)