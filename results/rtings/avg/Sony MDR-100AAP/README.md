# Sony MDR-100AAP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.9dB
GraphicEQ: 21 -1.9; 23 -2.4; 25 -2.8; 28 -3.4; 31 -3.9; 34 -4.3; 37 -4.5; 41 -4.7; 45 -4.8; 49 -4.8; 54 -4.9; 60 -5.0; 66 -5.0; 72 -5.0; 79 -5.2; 87 -5.6; 96 -6.0; 106 -6.3; 116 -6.5; 128 -6.5; 141 -6.3; 155 -6.1; 170 -5.9; 187 -5.4; 206 -4.6; 227 -3.4; 249 -3.3; 274 -4.4; 302 -3.3; 332 -2.1; 365 -1.2; 402 -0.7; 442 -0.6; 486 -0.6; 535 -0.6; 588 -0.6; 647 -0.6; 712 -0.4; 783 -0.3; 861 -0.2; 947 -0.1; 1042 0.1; 1146 0.1; 1261 0.0; 1387 -0.0; 1526 -0.1; 1678 -0.2; 1846 -0.0; 2031 0.1; 2234 0.9; 2457 1.8; 2703 2.4; 2973 2.8; 3270 1.7; 3597 1.0; 3957 0.5; 4353 0.4; 4788 1.9; 5267 -2.4; 5793 -0.4; 6373 0.4; 7010 1.5; 7711 0.3; 8482 -1.8; 9330 -0.5; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.8; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-100AAP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-29**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-100AAP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 45 Hz    |  0.56 | -4.1 dB |
| Peaking | 140 Hz   |  0.92 | -5.4 dB |
| Peaking | 282 Hz   |  5.18 | -2.0 dB |
| Peaking | 2868 Hz  |  3.15 | 3.0 dB  |
| Peaking | 4731 Hz  | 10.6  | 3.0 dB  |
| Peaking | 5278 Hz  |  6.51 | -3.2 dB |
| Peaking | 7107 Hz  |  3.18 | 1.4 dB  |
| Peaking | 8623 Hz  |  6.82 | -2.5 dB |
| Peaking | 18653 Hz |  4    | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-100AAP/Sony%20MDR-100AAP.png)