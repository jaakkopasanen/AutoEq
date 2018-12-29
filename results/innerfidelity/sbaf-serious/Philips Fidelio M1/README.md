# Philips Fidelio M1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.0; 25 2.7; 28 2.2; 31 1.7; 34 1.4; 37 1.1; 41 0.7; 45 0.4; 49 0.1; 54 -0.2; 60 -0.6; 66 -1.0; 72 -1.4; 79 -1.8; 87 -2.2; 96 -2.6; 106 -2.8; 116 -2.9; 128 -3.3; 141 -3.9; 155 -4.2; 170 -3.8; 187 -3.7; 206 -3.3; 227 -2.5; 249 -1.6; 274 -0.6; 302 0.1; 332 0.9; 365 1.7; 402 2.2; 442 2.6; 486 2.5; 535 2.4; 588 2.3; 647 1.8; 712 1.0; 783 0.8; 861 0.3; 947 -0.0; 1042 0.0; 1146 0.7; 1261 1.7; 1387 2.1; 1526 1.2; 1678 1.6; 1846 2.1; 2031 2.2; 2234 2.6; 2457 3.1; 2703 1.6; 2973 1.4; 3270 1.4; 3597 1.0; 3957 0.8; 4353 0.6; 4788 1.6; 5267 4.6; 5793 6.0; 6373 4.0; 7010 2.2; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.9; 20000 -0.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio M1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio M1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.84 | 3.7 dB  |
| Peaking | 165 Hz   | 0.72 | -4.5 dB |
| Peaking | 423 Hz   | 1.13 | 3.9 dB  |
| Peaking | 2168 Hz  | 1.52 | 2.5 dB  |
| Peaking | 5787 Hz  | 4.15 | 6.3 dB  |
| Peaking | 986 Hz   | 3.84 | -1.0 dB |
| Peaking | 1352 Hz  | 4.42 | 1.9 dB  |
| Peaking | 1491 Hz  | 3.61 | -0.8 dB |
| Peaking | 18694 Hz | 2.88 | -2.0 dB |
| Peaking | 20536 Hz | 2.26 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20M1/Philips%20Fidelio%20M1.png)