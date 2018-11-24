# Jabra Elite Active 65t

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.5; 28 4.6; 31 3.7; 34 3.1; 37 2.6; 41 2.2; 45 1.9; 49 1.6; 54 1.3; 60 0.8; 66 0.3; 72 0.0; 79 -0.3; 87 -0.8; 96 -1.3; 106 -1.9; 116 -2.5; 128 -2.9; 141 -3.3; 155 -3.7; 170 -3.8; 187 -3.9; 206 -3.8; 227 -3.7; 249 -3.6; 274 -3.3; 302 -2.9; 332 -2.6; 365 -2.3; 402 -2.1; 442 -1.5; 486 -0.9; 535 -0.3; 588 0.4; 647 1.2; 712 1.6; 783 1.3; 861 0.7; 947 0.3; 1042 -0.3; 1146 -1.0; 1261 -1.3; 1387 -1.3; 1526 -1.3; 1678 -1.5; 1846 -1.9; 2031 -2.1; 2234 -1.7; 2457 -1.1; 2703 -0.7; 2973 -0.6; 3270 -0.6; 3597 -0.7; 3957 -1.0; 4353 -1.8; 4788 -2.3; 5267 -2.2; 5793 -0.8; 6373 0.4; 7010 1.4; 7711 0.1; 8482 -2.8; 9330 -6.4; 10263 -8.2; 11289 -5.9; 12418 -2.0; 13660 -0.0; 15026 -0.1; 16529 -3.7; 18182 -5.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite Active 65t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite Active 65t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.7  | 6.4 dB  |
| Peaking | 188 Hz   | 0.87 | -4.4 dB |
| Peaking | 1982 Hz  | 1.7  | -2.0 dB |
| Peaking | 10241 Hz | 3.43 | -9.0 dB |
| Peaking | 17772 Hz | 3.08 | -6.1 dB |
| Peaking | 376 Hz   | 2.41 | -0.8 dB |
| Peaking | 705 Hz   | 2.91 | 2.4 dB  |
| Peaking | 4892 Hz  | 3.36 | -2.3 dB |
| Peaking | 7018 Hz  | 5.06 | 2.8 dB  |
| Peaking | 20252 Hz | 3.07 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%20Active%2065t/Jabra%20Elite%20Active%2065t.png)