# Sony WI-SP500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 5.0; 72 4.0; 79 2.9; 87 1.8; 96 0.7; 106 -0.3; 116 -1.2; 128 -1.9; 141 -2.5; 155 -2.9; 170 -3.2; 187 -3.5; 206 -3.7; 227 -3.9; 249 -3.9; 274 -3.9; 302 -3.9; 332 -3.9; 365 -3.9; 402 -4.0; 442 -4.0; 486 -3.7; 535 -3.5; 588 -3.1; 647 -2.4; 712 -1.5; 783 -0.7; 861 -0.0; 947 0.1; 1042 -0.0; 1146 0.0; 1261 0.2; 1387 0.3; 1526 0.4; 1678 0.5; 1846 0.5; 2031 0.2; 2234 -0.2; 2457 -0.2; 2703 0.9; 2973 3.3; 3270 5.5; 3597 6.0; 3957 4.9; 4353 2.0; 4788 -0.6; 5267 -3.9; 5793 -2.4; 6373 1.6; 7010 2.3; 7711 0.2; 8482 -2.5; 9330 -1.5; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-SP500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-SP500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.39 | 9.8 dB  |
| Peaking | 155 Hz  | 0.37 | -7.6 dB |
| Peaking | 3585 Hz | 2.81 | 6.7 dB  |
| Peaking | 5011 Hz | 6.91 | -2.4 dB |
| Peaking | 5457 Hz | 9.7  | -4.9 dB |
| Peaking | 548 Hz  | 1.28 | -3.5 dB |
| Peaking | 681 Hz  | 0.72 | 2.7 dB  |
| Peaking | 2421 Hz | 5.07 | -1.6 dB |
| Peaking | 6827 Hz | 7.38 | 3.1 dB  |
| Peaking | 8700 Hz | 6.22 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20WI-SP500/Sony%20WI-SP500.png)