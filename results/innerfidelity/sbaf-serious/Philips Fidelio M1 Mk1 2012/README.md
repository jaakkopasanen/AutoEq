# Philips Fidelio M1 Mk1 2012

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.3; 25 0.1; 28 -0.0; 31 -0.1; 34 -0.1; 37 -0.1; 41 -0.1; 45 -0.1; 49 -0.1; 54 -0.0; 60 0.1; 66 0.2; 72 0.2; 79 0.0; 87 -0.2; 96 -0.3; 106 -0.1; 116 0.2; 128 0.4; 141 0.5; 155 0.8; 170 1.6; 187 1.9; 206 2.1; 227 2.3; 249 2.4; 274 2.6; 302 2.8; 332 2.6; 365 2.0; 402 1.5; 442 0.7; 486 -0.0; 535 -0.3; 588 -0.2; 647 -0.4; 712 -0.4; 783 -0.1; 861 -0.1; 947 -0.0; 1042 0.1; 1146 0.4; 1261 0.6; 1387 0.5; 1526 0.4; 1678 0.5; 1846 1.0; 2031 1.9; 2234 2.8; 2457 4.0; 2703 4.9; 2973 5.8; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio M1 Mk1 2012 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio M1 Mk1 2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 278 Hz  | 0.85 | 5.6 dB  |
| Peaking | 335 Hz  | 0.44 | -2.8 dB |
| Peaking | 3351 Hz | 1.31 | 6.1 dB  |
| Peaking | 5606 Hz | 2.75 | 4.7 dB  |
| Peaking | 1725 Hz | 1.17 | 1.0 dB  |
| Peaking | 1730 Hz | 2.57 | -1.7 dB |
| Peaking | 6524 Hz | 7.22 | 1.7 dB  |
| Peaking | 6716 Hz | 5.84 | 0.8 dB  |
| Peaking | 7681 Hz | 1.99 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20M1%20Mk1%202012/Philips%20Fidelio%20M1%20Mk1%202012.png)