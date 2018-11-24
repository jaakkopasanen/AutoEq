# Logitech UE4000 2012

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.0; 25 -0.1; 28 -0.2; 31 -0.4; 34 -0.5; 37 -0.6; 41 -0.6; 45 -0.7; 49 -0.8; 54 -0.9; 60 -1.0; 66 -1.1; 72 -1.4; 79 -1.7; 87 -1.9; 96 -2.0; 106 -2.0; 116 -2.8; 128 -2.7; 141 -2.2; 155 -2.5; 170 -2.1; 187 -2.3; 206 -2.5; 227 -2.0; 249 -1.2; 274 -0.0; 302 0.9; 332 1.9; 365 2.6; 402 2.6; 442 2.5; 486 1.9; 535 1.5; 588 1.3; 647 0.6; 712 -0.0; 783 -0.0; 861 -0.3; 947 0.3; 1042 -0.1; 1146 0.3; 1261 1.0; 1387 1.5; 1526 2.3; 1678 3.1; 1846 4.6; 2031 5.9; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech UE4000 2012 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE4000 2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 58 Hz   | 1.32 | 0.3 dB  |
| Peaking | 225 Hz  | 3.41 | -1.0 dB |
| Peaking | 351 Hz  | 0.27 | -5.1 dB |
| Peaking | 400 Hz  | 0.89 | 7.5 dB  |
| Peaking | 2986 Hz | 0.6  | 7.5 dB  |
| Peaking | 1313 Hz | 1.3  | -0.6 dB |
| Peaking | 2034 Hz | 4.32 | 1.5 dB  |
| Peaking | 3128 Hz | 2.33 | -1.0 dB |
| Peaking | 6207 Hz | 1.99 | 5.8 dB  |
| Peaking | 7466 Hz | 1.42 | -4.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE4000%202012/Logitech%20UE4000%202012.png)