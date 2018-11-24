# Polk Audio UltraFit 2000 sample A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.3; 60 3.8; 66 2.5; 72 1.4; 79 0.3; 87 -0.7; 96 -1.5; 106 -2.0; 116 -2.2; 128 -2.4; 141 -2.6; 155 -2.5; 170 -2.3; 187 -1.9; 206 -1.5; 227 -1.1; 249 -0.7; 274 -0.3; 302 0.4; 332 1.0; 365 1.6; 402 2.4; 442 2.5; 486 3.1; 535 3.5; 588 4.1; 647 4.4; 712 4.3; 783 3.5; 861 1.9; 947 0.2; 1042 0.1; 1146 -0.9; 1261 -1.2; 1387 -0.9; 1526 -2.6; 1678 -2.7; 1846 -1.4; 2031 0.5; 2234 2.7; 2457 5.2; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.9; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.43 | 8.5 dB  |
| Peaking | 108 Hz  | 0.66 | -6.9 dB |
| Peaking | 599 Hz  | 1.15 | 4.8 dB  |
| Peaking | 1618 Hz | 1.31 | -6.7 dB |
| Peaking | 3236 Hz | 0.72 | 8.0 dB  |
| Peaking | 961 Hz  | 9.16 | -1.2 dB |
| Peaking | 2530 Hz | 6.83 | 1.5 dB  |
| Peaking | 3585 Hz | 2.86 | -1.2 dB |
| Peaking | 6335 Hz | 2.11 | 5.7 dB  |
| Peaking | 7312 Hz | 1.45 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%202000%20sample%20A/Polk%20Audio%20UltraFit%202000%20sample%20A.png)