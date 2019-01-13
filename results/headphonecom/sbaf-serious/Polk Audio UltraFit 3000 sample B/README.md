# Polk Audio UltraFit 3000 sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -10.6; 23 -10.7; 25 -10.8; 28 -10.9; 31 -11.0; 34 -11.1; 37 -11.0; 41 -11.1; 45 -11.1; 49 -11.2; 54 -11.2; 60 -11.3; 66 -11.3; 72 -11.4; 79 -11.4; 87 -11.3; 96 -11.2; 106 -11.0; 116 -10.8; 128 -10.7; 141 -10.4; 155 -10.1; 170 -9.6; 187 -9.2; 206 -8.7; 227 -8.1; 249 -7.5; 274 -6.9; 302 -6.1; 332 -5.4; 365 -4.6; 402 -3.8; 442 -3.2; 486 -2.6; 535 -1.9; 588 -1.3; 647 -0.6; 712 -0.2; 783 0.2; 861 0.7; 947 0.3; 1042 -0.0; 1146 -0.2; 1261 -0.8; 1387 -1.5; 1526 -2.5; 1678 -3.2; 1846 -3.7; 2031 -4.2; 2234 -4.3; 2457 -3.7; 2703 -2.4; 2973 -0.8; 3270 0.8; 3597 1.3; 3957 1.3; 4353 3.1; 4788 5.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 3000 sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 3000 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.38 | -8.1 dB |
| Peaking | 117 Hz  | 0.32 | -9.8 dB |
| Peaking | 772 Hz  | 0.87 | 2.7 dB  |
| Peaking | 2058 Hz | 1.55 | -5.0 dB |
| Peaking | 5333 Hz | 2.08 | 7.1 dB  |
| Peaking | 2547 Hz | 5.99 | -0.6 dB |
| Peaking | 3303 Hz | 5.8  | 1.3 dB  |
| Peaking | 6512 Hz | 5.29 | 3.3 dB  |
| Peaking | 7269 Hz | 1.82 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%203000%20sample%20B/Polk%20Audio%20UltraFit%203000%20sample%20B.png)