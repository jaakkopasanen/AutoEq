# Philips Fidelio X2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.0; 25 2.1; 28 1.0; 31 -0.1; 34 -1.0; 37 -1.8; 41 -2.6; 45 -3.4; 49 -3.9; 54 -4.4; 60 -4.8; 66 -5.0; 72 -5.2; 79 -5.3; 87 -5.2; 96 -5.1; 106 -4.7; 116 -4.1; 128 -3.7; 141 -3.5; 155 -3.4; 170 -2.8; 187 -2.6; 206 -3.1; 227 -4.1; 249 -3.3; 274 -2.8; 302 -2.6; 332 -2.4; 365 -2.3; 402 -2.2; 442 -2.0; 486 -2.3; 535 -2.3; 588 -2.1; 647 -2.2; 712 -2.2; 783 -1.8; 861 -1.4; 947 -0.4; 1042 0.3; 1146 1.2; 1261 1.1; 1387 -0.3; 1526 -2.3; 1678 -2.7; 1846 -2.3; 2031 -1.5; 2234 -1.6; 2457 -0.9; 2703 1.9; 2973 3.4; 3270 1.5; 3597 1.0; 3957 -0.1; 4353 -2.9; 4788 -3.8; 5267 3.2; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.0; 8482 -5.3; 9330 -6.6; 10263 -1.1; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio X2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio X2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  1.2  | 5.9 dB  |
| Peaking | 68 Hz   |  0.93 | -3.1 dB |
| Peaking | 128 Hz  |  0.16 | -2.8 dB |
| Peaking | 6143 Hz |  4.63 | 7.3 dB  |
| Peaking | 9012 Hz |  5.15 | -8.2 dB |
| Peaking | 1215 Hz |  2.37 | 5.7 dB  |
| Peaking | 1508 Hz |  1.11 | -4.2 dB |
| Peaking | 2949 Hz |  4.16 | 4.8 dB  |
| Peaking | 4723 Hz |  6.12 | -5.8 dB |
| Peaking | 5509 Hz | 10.15 | 4.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20X2/Philips%20Fidelio%20X2.png)