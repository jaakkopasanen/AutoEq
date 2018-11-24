# Noontec Zoro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.0; 23 -0.4; 25 -0.7; 28 -1.0; 31 -1.3; 34 -1.5; 37 -1.7; 41 -1.9; 45 -2.1; 49 -2.2; 54 -2.4; 60 -2.6; 66 -2.8; 72 -3.1; 79 -3.4; 87 -3.7; 96 -3.9; 106 -4.2; 116 -4.3; 128 -4.5; 141 -4.6; 155 -4.7; 170 -4.7; 187 -4.7; 206 -4.7; 227 -4.7; 249 -4.5; 274 -4.2; 302 -3.9; 332 -3.9; 365 -3.8; 402 -3.5; 442 -3.2; 486 -3.3; 535 -3.0; 588 -2.5; 647 -2.1; 712 -1.6; 783 -0.8; 861 -0.3; 947 -0.0; 1042 -0.0; 1146 -0.1; 1261 -0.1; 1387 -1.0; 1526 -1.8; 1678 -1.5; 1846 -0.6; 2031 1.2; 2234 3.1; 2457 5.5; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.7; 6373 4.3; 7010 2.3; 7711 -1.4; 8482 -2.3; 9330 -0.3; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 91 Hz    | 0.45 | -1.8 dB |
| Peaking | 270 Hz   | 0.36 | -3.8 dB |
| Peaking | 1690 Hz  | 2.06 | -5.9 dB |
| Peaking | 3383 Hz  | 0.48 | 7.5 dB  |
| Peaking | 8387 Hz  | 2.94 | -5.8 dB |
| Peaking | 2223 Hz  | 4.89 | -1.1 dB |
| Peaking | 2478 Hz  | 3.92 | 1.6 dB  |
| Peaking | 3629 Hz  | 1.77 | -0.9 dB |
| Peaking | 5699 Hz  | 3.18 | 1.3 dB  |
| Peaking | 12998 Hz | 1.54 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro/Noontec%20Zoro.png)